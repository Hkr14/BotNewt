from sample_config import Config


class Development(Config):
  # get this values from my.telegram.org. 
  # 6 is just a placeholder. Fill your own api id & hash.
  APP_ID = 13532780
  API_HASH = "f73ffaec3acf05270cde1dc63c561ef0"

  # the name to display in your alive message.
  # If not filled anything then default value is Mafia User.
  ALIVE_NAME = "Mafia User"
  ABUSE = "OFF"
  BAN_PIC = "https://telegra.ph/"
  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgres://fkgwwfvr:gizJf7gFUrfzJcYI3HTzyWhQAZWlrpqe@salt.db.elephantsql.com/fkgwwfvr"

  # After cloning the repo and installing requirements...
  # Do python string_session.py and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  STRING_SESSION = "1AZWarzUBu1yeNStTzzl-odMQL87FdGLape4D3fkY3ZWfHtsDSctwjQJ29pnCxtKIohdMIsK93L9G9Azp44HErJApRch5ry9FGJkCUKytt3Z1ftsIls5BI06UmO4TKKSQD3QbGuJ2KHlX-0HVDhM1JPC4Y4GMKzTI8QyMVmlf0oY81zDzKrBilmI92j7C5f54yEv0uibnBKVfDsYFer1hoqkfMvv7U3oKT2yNNA3VghDyCHSDfNGVcbhe0D923UcYQdPSBJxhJ1MFKOCMiShWL__WXCknIPxUqK5UJADKB1U9N5NK07HEXuqVRO1eajd-6ZjXPtx5bzoDKvL-FUYY-Bl3zVASbuk="

  # Create a bot in @botfather and fill the following values with bot token and username.
  TG_BOT_TOKEN_BF_HER = "5578003206:AAGIrqIrOUn_83nMVM4w_YpXZCLV_8sewrI" #token
  TG_BOT_USER_NAME_BF_HER = "AlphaBot" #username

  # Create a private group and add rose bot to it.
  # and type /id and paste that id here.
  # replace that -100 with that group id.
  PRIVATE_GROUP_BOT_API_ID = -100
          MAFIABOT_LOGGER = -1001799034168
  # Custom Command Handler. 
  COMMAND_HAND_LER = "."

  # enter the userid of sudo users.
  # you can add multiple ids by separating them by space.
  # fill values in [] only.
  SUDO_USERS = [1924666696]

  # command hanler for sudo users.
  SUDO_COMMAND_HAND_LER = "."
  
  
