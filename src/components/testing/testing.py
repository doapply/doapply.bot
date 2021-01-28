import discord
from discord.ext import commands
from config import version
import sys

from utils.utilities import get_uptime


class Testing(commands.Cog):
    '''
    General purpose commands for testing the bot.
    '''
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.command()
    async def status(self, ctx: commands.Context):
        '''
        Shows the current status of the bot
        '''
        await ctx.send(f"**Uptime**: {round(get_uptime(), 1)}s\n"
                       f"**Version**: {version}\n"
                       f"Currently Connected to **{len(self.bot.guilds)}** "
                       f"**API Latency**: {round(self.bot.latency, 4)}s\n"
                       f"Running discord.py version {discord.__version__}")

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx: commands.Context):
        '''
        Restarts the bot on the remote host
        '''
        await ctx.send("Restarting...")
        await self.bot.change_presence(status=discord.Status.offline)
        await self.bot.logout()
        sys.exit(0)
