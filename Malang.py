import os,platform
os.system('git pull')
print("Join Whatapss group")
os.system('xdg-open https://chat.whatsapp.com/Fw5JNUdDbuPCtAHLrhLpt3')
os.system("clear")
xyz=platform.architecture()[0]
if xyz=="32bit":
    __import__("B2")
elif xyz=="64bit":
    __import__("B2")