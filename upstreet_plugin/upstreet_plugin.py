from upstreet import Agent
import os
from typing import TypedDict
from colorama import Fore

description = "An AutoGPT upstreet bot that allows users to interact with their AutoGPT instance through upstreet."

userReply = []
messagesToSend = []
waitingForReply = [False]

finishedLoggingIn = [False]

class Message(TypedDict):
    role: str
    content: str

class AutoGPT_Upstreet():
    def __init__(self):
        self.agent = Agent()

    async def on_ready(self):
        await self.agent.connect()
        print(Fore.GREEN + f'Bot logged in as {self.user} (ID: {self.user.id})')
        print(Fore.GREEN + '------')
        finishedLoggingIn[0] = True

    async def setup_hook(self) -> None:
        self.background.start()
    
    @tasks.loop(seconds=1) 
    async def background(self):
        print('Background loop...')
        # pop a message from messagesToSend
        if len(messagesToSend) > 0:
            message = messagesToSend.pop(0)
            print('Sending message: ' + message)
            await self.agent.speak(message)

    async def on_message(self, message):
        await self.agent.speak(message)
    
def commandUnauthorized(feedback):
    return "This command was not authorized by the user. Do not try it again. Here is the provided feedback: " + feedback

def run_bot():
    global client
    client = AutoGPT_Upstreet()
