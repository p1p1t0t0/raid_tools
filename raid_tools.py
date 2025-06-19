import discord
import asyncio
from discord.ext import commands
from colorama import Fore, init
import os

init(autoreset=True)
os.system("cls" if os.name == "nt" else "clear")

print(Fore.MAGENTA + """
╔═══════════════════════════════╗
║       🔧 DISCORD TOOL         ║
║       by @p1p1t0t0_off        ║
╚═══════════════════════════════╝
""")

token = input(Fore.CYAN + "🔑 Entre le token de ton bot : " + Fore.LIGHTBLUE_EX)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(Fore.GREEN + f"\n✅ Connecté en tant que {bot.user}")
    server_id = input(Fore.CYAN + "\n🏠 ID du serveur cible : " + Fore.LIGHTBLUE_EX)

    try:
        server = bot.get_guild(int(server_id))
        if not server:
            raise ValueError
    except:
        print(Fore.RED + "❌ Identifiant invalide")
        await bot.close()
        return

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.MAGENTA + """
╔═══════════════════════════════╗
║         MENU PRINCIPAL        ║
╚═══════════════════════════════╝

1. Supprimer tous les salons
2. Supprimer tous les rôles
3. Supprimer tous les emojis
4. Créer des salons
5. Créer des rôles
6. Modifier tous les pseudos

""")
        choix = input(Fore.YELLOW + "Sélectionne une option : ")

        if choix == "1":
            for channel in server.channels:
                try:
                    await channel.delete()
                    print(Fore.RED + f"Supprimé : {channel.name}")
                except:
                    pass

        elif choix == "2":
            for role in server.roles[::-1]:
                if role != server.default_role:
                    try:
                        await role.delete()
                        print(Fore.RED + f"Supprimé : {role.name}")
                    except:
                        pass

        elif choix == "3":
            for emoji in server.emojis:
                try:
                    await emoji.delete()
                    print(Fore.RED + f"Supprimé : {emoji.name}")
                except:
                    pass

        elif choix == "4":
            nom = input("Nom des salons à créer : ")
            nombre = int(input("Nombre : "))
            for _ in range(nombre):
                await server.create_text_channel(nom)
                print(Fore.GREEN + f"Créé : {nom}")

        elif choix == "5":
            nom = input("Nom des rôles : ")
            couleur = input("Code couleur (#HEX ou none) : ")
            admin = input("Administrateur ? (Y/N) : ")
            perms = discord.Permissions(administrator=True) if admin.upper() == "Y" else discord.Permissions.none()
            color = discord.Colour.default() if couleur.lower() == "none" else discord.Colour(int(couleur.replace("#", "0x"), 16))
            role = await server.create_role(name=nom, permissions=perms, colour=color)
            print(Fore.GREEN + f"Créé : {role.name}")

        elif choix == "6":
            nouveau = input("Nouveau pseudo à appliquer : ")
            for member in server.members:
                try:
                    await member.edit(nick=nouveau)
                    print(Fore.YELLOW + f"Modifié : {member}")
                except:
                    pass

bot.run(token)
