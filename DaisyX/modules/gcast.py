from DaisyX.function.pluginhelpers import admins_only
from DaisyX.services.pyrogram import pbot
import asyncio

from DaisyX.services.pyrogram import Client
from DaisyX.services.pyrogram import filters

from DaisyX.services.pyrogram.types import Dialog 
from DaisyX.services.pyrogram.types import Chat
from DaisyX.services.pyrogram.types import Message

from DaisyX.Services.pyrogram.errors import UserAlreadyParticipant

from DaisyX import DEV_USERS

@pbot.on_message(filters.command(["gcast"]))

async def broadcast(_, message: Message):

    sent=0

    failed=0

    if message.from_user.id not in DEV_USERS:

        return

    else:

        wtf = await message.reply("`starting broadcast...`")

        if not message.reply_to_message:

            await wtf.edit("please reply to a message to start broadcast!")

            return

        lmao = message.reply_to_message.text

        async for dialog in pbot.iter_dialogs():

            try:

                await pbot.send_message(dialog.chat.id, lmao)

                sent = sent+1

                await wtf.edit(f"`broadcasting...` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats")

                await asyncio.sleep(3)

            except:

                failed=failed+1

        await message.reply_text(f"`gcast succesfully` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats")
