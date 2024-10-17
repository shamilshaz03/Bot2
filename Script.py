class script(object):
    START_TXT = """<b><i>𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 🔞 ᴍᴀʟᴀʏᴀʟᴀᴍ & ᴇᴛᴄ videos , 𝙴𝙽𝙹𝙾𝚈 😍</b></i>"""
    HELP_TXT = """<b>𝙷𝙴𝚈 {}
𝟽𝟼𝟶𝟶𝟶+ ᴠɪᴅᴇᴏs ᴏɴʟʏ 𝟹𝟿𝟿₹ 
ᴀʟʟ ᴛʏᴘᴇ ᴠɪᴅᴇᴏs ᴀᴠᴀɪʟᴀʙʟᴇ.</b>"""
    ABOUT_TXT = """<b>✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/xmallu_admin>Creator</a>
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: ᴘʀɪᴠᴀᴛᴇ sᴇʀᴠᴇʀ
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0 [ 𝙱𝙴𝚃𝙰 ]</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- 😂 </b>
<b>DEVS:</b>
- 😭"""
    TELEGRAPH = """Reply to any photo or video using by /telegraph that photo telegraph link you will get"""
    TOOLS = """TOOLS:

𝟷𝟼𝟶𝟶𝟶+ ᴠɪᴅᴇᴏs ᴏɴʟʏ 𝟷𝟿𝟿₹ 
ᴀʟʟ ᴛʏᴘᴇ ᴠɪᴅᴇᴏs ᴀᴠᴀɪʟᴀʙʟᴇ"""
    LYRICS = """Usage Lyrics:

/lyrics - {song name}"""
    QRCODE = """Usage qr code:

/qr - {text}"""
    SONG = """usage song: 

/song - {song name}"""
    IMAGINE = """ How to Use example
<code>/imagine a boy and girl looking a sky </code>
You Can Create Your like pictures using by This command /imagine """
    TRANSLATE = """Usages:
/tr reply message and ml like this

<code> /tr ml </code>"""
    PROMOTE = """<b>Yᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ᴍᴇᴍʙᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ
 
Bʏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ. 
/promote 


Yᴏᴜ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ ᴛʜᴇᴍ ʙʏ ᴀᴅᴍɪɴ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ /demote</b>"""
    IMG = """ You Can Serch Image Using This command /img
Example: <code> /image Tony stark </code>"""
    FONT_TXT = """ ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴜɴᴄᴛɪᴏɴ

/font {your_text}

ᴇɢ:- /font Hello """
    STICKER = """ yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ꜰɪɴᴅᴀɴy  ꜱᴛɪᴄᴋᴇʀꜱ ɪᴅ.
• ᴜꜱᴀɢᴇ :ᴛᴏ ɢᴇᴛ ꜱᴛɪᴄᴋᴇʀ
 
⭕ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ
◉ Reply To Any Sticker [/stickerid]"""
    TTS = """ Help:  TTS 🎤 module:
Translate text to speech
Commands and Usage:
• /tts  : convert text to speech"""
    BUG_TXT = """Yᴏᴜ ᴄᴀɴ ʀᴇᴘᴏʀᴛ ᴇʀʀᴏʀs ᴀɴᴅ ʙᴜɢs ᴡɪᴛʜ ᴛʜᴇ ʙᴏᴛ 
ᴜsɪɴɢ ʙʏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ /bug """
    FEED = """Iғ Yᴏᴜ Wᴀɴᴛ Aɴʏ Fᴇᴇᴅʙᴀᴄᴋ ᴏʀ Aɴʏ Fᴇᴄᴛᴜʀᴇs Aʙᴏᴜᴛ Tʜᴇ Bᴏᴛ, 
Jᴜsᴛ Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ /feedback"""
    AI = """AI
/openai {query}
"""
    FUNS = """FUNS HELP

/truth - [message]
/dare - [message]
/joke - [message]
"""
    ECHO = """ Tʜɪs ғᴇᴄᴛᴜʀᴇ ɪs ᴠᴇʀʏ ɪɴᴛᴇʀᴇsᴛɪɴɢ ᴀɴᴅ ғᴜɴɴʏ 

 Tʜᴇ MEMBERS ᴏғ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʀᴇᴘʟʏ ᴛᴇxᴛ

 Tʜᴀᴛ ᴡɪʟʟ sʜᴏᴡ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ʀᴇᴘʟʏᴇᴅ ᴀɴᴅ ᴛʜᴇɴ ᴏᴜʀ ᴍᴇssᴀɢᴇ ᴅᴇʟᴇᴛᴇ ᴡɪʟʟ 
 /echo {text}
 """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    ENHANCE = """ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ᴜsɪɴɢ ʙʏ /enhance ᴀɴᴅ ᴛʜᴀᴛ ᴘʜᴏᴛᴏ ᴡɪʟʟ ᴇɴʜᴀɴᴄᴇᴅ"""
    CARBON = """HELP: Carbon

Beautify your code using carbon!

USAGE:
➢ /carbon [text] - Create carbon from the given text."""
    BUTTON_TXT = """Help: <b>Buttons</b>

- bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/....)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    PONG_TXT = """ ᴘɪɴɢ ᴛᴇꜱᴛɪɴɢ:ʜᴇʟᴘꜱ ʏᴏᴜ ᴛᴏ ᴋɴᴏᴡ ʏᴏᴜʀ ᴘɪɴɢ🪄

ᴄᴏᴍᴍᴀɴᴅꜱ:
• /alive - ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜ ᴀʀᴇ ᴀʟɪᴠᴇ.
• /ping - ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴘɪɴɢ.

ᴜꜱᴀɢᴇ :
• ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ɪɴ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘꜱ
• ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ʙᴜʏ ᴇᴠᴇʀʏᴏɴᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ʙᴏᴛꜱ ᴘᴍ
• ꜱʜᴀʀᴇ ᴜꜱ ꜰᴏʀ ᴍᴏʀᴇ ꜰᴇᴀᴛᴜʀᴇꜱ"""
    PIN_TXT = """ ᴩɪɴ ᴍᴏᴅᴜʟᴇ
ᴩɪɴ ᴀ ᴍᴇꜱꜱᴀɢᴇ...

ᴀʟʟ ᴛʜᴇ ᴩɪɴ ʀᴇᴩʟᴀᴛᴇᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ꜰᴏᴜɴᴅ ʜᴇʀᴇ:

📌ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ📌

/pin :- ᴛᴏ ᴩɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ᴏɴ ʏᴏᴜʀ ᴄʜᴀᴛꜱ
/unpin :- ᴛᴏ ᴜɴᴩɪɴ ᴛʜᴇ ᴄᴜʀʀᴇᴇɴᴛ ᴩɪɴɴᴇᴅ ᴍᴇꜱꜱᴀɢ
/unpin_all :- ᴛᴏ ᴜɴᴩɪɴ ᴛʜᴇ ᴄᴜʀʀᴇᴇɴᴛ ᴩɪɴɴᴇᴅ ᴀʟʟ ᴍᴇꜱꜱᴀɢ"""
    CAPTION = """
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ : </b> {file_name}"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>"""

    FLTERS_TXT = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    
    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""
    
    GLOBAL_TXT = """ <b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
   
   Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
   
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    RENDERING_TXT = """
⚡️ʟɪᴠᴇ sʏsᴛᴇᴍ sᴛᴀᴛᴜs ⚡️

❂ ʀᴀᴍ ●●●●●●●◌◌◌
✇ ᴄᴘᴜ ●●●●●●●◌◌◌
✪ ᴅᴀᴛᴀ ᴛʀᴀꜰɪᴄs ●●●●◌◌◌◌◌◌ 🛰

ᴠ2.7.1 [sᴛᴀʙʟᴇ] """
    DICS_TXT = """ <b><code>ᴛʜɪꜱ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʀᴀɴsᴀᴄᴛɪᴏɴs ᴀʀᴇ ғɪɴᴀʟ, ᴀɴᴅ ᴡᴇ ᴅᴏ ɴᴏᴛ ᴏғғᴇʀ ʀᴇғᴜɴᴅs ᴜɴᴅᴇʀ ᴀɴʏ ᴄɪʀᴄᴜᴍsᴛᴀɴᴄᴇs.
ʙʏ ᴜsɪɴɢ ᴏᴜʀ sᴇʀᴠɪᴄᴇ, ʏᴏᴜ ᴀᴄᴄᴇᴘᴛ ғᴜʟʟ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ ғᴏʀ ʏᴏᴜʀ ᴀᴄᴛɪᴏɴs ᴀɴᴅ ᴅᴇᴄɪsɪᴏɴs. 
ᴘʟᴇᴀsᴇ ɴᴏᴛᴇ ᴛʜᴀᴛ ᴏᴜʀ sᴇʀᴠɪᴄᴇ ᴍᴀʏ ᴏᴄᴄᴀsɪᴏɴᴀʟʟʏ ʙᴇ ᴜɴᴀᴠᴀɪʟᴀʙʟᴇ, 
ᴀɴᴅ ᴡʜɪʟᴇ ᴡᴇ sᴛʀɪᴠᴇ ғᴏʀ ʀᴇʟɪᴀʙɪʟɪᴛʏ, ᴡᴇ ᴄᴀɴɴᴏᴛ ɢᴜᴀʀᴀɴᴛᴇᴇ ᴄᴏɴᴛɪɴᴜᴏᴜs ᴀᴄᴄᴇss. 
ᴡᴇ ᴛᴀᴋᴇ ᴘʀɪᴅᴇ ɪɴ ʙᴇɪɴɢ ᴏɴᴇ ᴏғ ᴛʜᴇ ғᴀsᴛᴇsᴛ ᴀɴᴅ ᴍᴏsᴛ ᴘᴏᴘᴜʟᴀʀ ʙᴏᴛs ᴀᴠᴀɪʟᴀʙʟᴇ, 
ᴛʜᴏᴜɢʜ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴇxᴘᴇʀɪᴇɴᴄᴇs ᴍᴀʏ ᴠᴀʀʏ. </code> """

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Tony Stark 

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /group_broadcast - <code>to broadcast a message to all groups</code>
• /eval - <code>run python codes</code>
• /sh - <code>install package or other use and code run</code>
• /restart - <code>restart the bot</code>
"""
    ALRT_TXT = """Hᴇʟʟᴏ {},

Tʜɪs ɪs ɴᴏᴛ ʏᴏᴜʀ ʀᴇϙᴜᴇsᴛ.
Rᴇϙᴜᴇsᴛ ʏᴏᴜʀsᴇʟғ...!!"""

    OLD_ALRT_TXT = """Hey {},
You are using one of old message,
Request Again"""

    CUDNT_FND = """<b>I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ. Dɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏғ ᴛʜᴇsᴇ?</b>"""

    I_CUDNT = """<b>I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.</b>"""

    I_CUD_NT = """<b>I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.</b>"""

    MVE_NT_FND = """<b>I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.</b>"""

    TOP_ALRT_MSG = """Cʜᴇᴄᴋɪɴɢ ғᴏʀ ϙᴜᴇʀʏ ɪɴ Dᴀᴛᴀʙᴀsᴇ """
    
    NORSLTS = """
#NoResults 

ID <b>: {}</b>

Name <b>: {}</b>

Message <b>: {}</b>"""
    
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: 17347
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: 1738
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: 631.96 GB G𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: 1024 GB G𝚒𝙱"""
    NORSLTS = """★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !
📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""
    
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
  
