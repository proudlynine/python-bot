import os

from utils import default
from utils.data import Bot, HelpFormat

config = default.get("config.json")
print("[INFO] Bot starting...")

bot = Bot(
    command_prefix=config.prefix,
    prefix=config.prefix,
    command_attrs=dict(hidden=True),
    help_command=HelpFormat()
)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")
        print(f'[INFO] Loaded extension: {name}')

bot.run(config.token)
