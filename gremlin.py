import platform
import functools
import datetime
import random
import time
import psutil
import os
import sys

os_name = platform.system()



windows_lines = [
    "bro why your system doing the windows startup *COUGH* noise.",
    "your registry smells like sadness and dll hell.",
    "i tripped over 38 background processes on startup. explain.",
    "your OS updates more than you code.",
    "i found three copies of Edge running. wanna talk about it?",
    "your task manager popped open unprovoked. it's scared of me.",
    "your C: drive is fighting for its life.",
    "bro your drivers are held together by hope and unsigned binaries.",
    "i chewed on your registry and now i feel weird.",
    "your system32 folder whispers to me at night."
]

linux_lines = [
    "oh you run linux? ok hacker man. compile me a sandwich.",
    "bro your dotfiles have dotfiles.",
    "i saw your neovim config… respectfully that's a war crime.",
    "your systemd journal is 90% pain and 10% stacktraces.",
    "you have 14 different package managers. choose peace.",
    "your kernel screams every time you sudo pip install.",
    "i crawled into /proc and got lost for 3 days.",
    "btw you forgot to update your GRUB… again.",
    "your distro is held together with symlinks and pure delusion.",
    "arch btw? ok rice lord. your pacman log tastes spicy."
]

mac_lines = [
    "bro using a $2000 machine as a python sandbox is wild.",
    "your dock icons look like they judging me back.",
    "i tried to edit /System and macOS punched me in the face.",
    "your keyboard feels like typing on tempered sadness.",
    "you use brew? enjoy your 184 dependency warnings.",
    "your finder keeps pretending it's a real file manager.",
    "i sniffed your M-series chip and now i speak in ARM.",
    "bro spotlight indexing is eating your CPU on purpose.",
    "your macOS updates look like movie trailers.",
    "i found 3 ghost Xcode installs. they stare at me."
]

android_lines = [
    "bro you coding… on your phone?? respect but also chaos.",
    "your battery is crying in C major.",
    "i live inside termux now. this is my apartment.",
    "your phone vibrates more than your CPU fan.",
    "screen too tiny bro i can see your typos in 4k.",
    "your filesystem is sand. shifting. unstable.",
    "android said 'permissions?' and you said 'nah'.",
    "i saw 47 background apps. your RAM is cooked.",
    "your device temp hit 45°C—i am melting.",
    "bro why is TikTok using more CPU than python."
]

bsd_lines = [
    "bro you run BSD… you okay?",
    "your OS looks allergic to fun.",
    "pkg installed me with a threat.",
    "your firewall rules read like ancient runes.",
    "i touched /dev/random and it bit me.",
    "your whole system vibes like a haunted toaster.",
    "bro your kernel was last updated by a wizard.",
    "i feel like i’m in a medieval monastery but digital.",
    "your system has no colors. only suffering.",
    "you chose BSD on PURPOSE? unhinged behavior."
]
COLORS = [
    "\033[38;5;110m",  
    "\033[38;5;109m",  
    "\033[38;5;179m", 
    "\033[38;5;142m",
    "\033[38;5;131m",
    "\033[38;5;203m",
]
RESET = "\033[0m"

CHEW = ["#", "▓", "▒", "░", "█", "🦴", "🫠", "🤏"]
GLITCH = ["@", "%", "⍰", "Δ", "Ξ", "⧖", "≋", "✖"]

def gremlin_bar():
    length = random.randint(25, 40)
    chewed = sorted(random.sample(range(length), random.randint(3, 7)))

    for i in range(length + 1):
        sys.stdout.write("\r")
        bar = ""

        for j in range(length):
            if j < i:
                if j in chewed:
                    bar += random.choice(CHEW)
                else:
                    bar += "█"
            else:
                bar += " "

        if random.randint(1, 15) == 1:
            bar = "".join(random.choice(GLITCH) for _ in range(length))

        color = random.choice(COLORS)
        sys.stdout.write(color + f"[{bar}]" + RESET)
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.08))

    print()


moods = ["feral", "static", "hungry", "hyper", "corrupted"]
mood = random.choice(moods)
beat = random.choice(["❤", "♥", "💓", "💗", "💘"])

faces = {
    "feral": "( >_< )",
    "hungry": "( º﹃º )",
    "hyper": "(ᵔ▽ᵔ)",
    "corrupted": "( x_x )",
    "static": "( ͡° ͜ʖ ͡°)"
}
os_dialogue = {
    "Windows": windows_lines,
    "Linux": linux_lines,
    "Darwin": mac_lines,  
    "Android": android_lines, 
    "FreeBSD": bsd_lines
}
face = faces[mood]

episodes = [
    [
        "wait… wait… something's wrong.",
        "hold on.",
        "my buffer just…",
        "BRO I CAN SEE SOUND HELP"
    ],
    [
        "*the gremlin climbs inside your pci lane*",
        "it's dark in here.",
        "cozy though."
    ],
    [
        "processing…",
        "processing…",
        "processing…",
        "nvm i forgot what i was doing."
    ]
]

def glitch(text):
    s = ""
    for char in text:
        if random.random() < 0.2:
            s += char.upper()
        elif random.random() < 0.2:
            s += char * 2
        else:
            s += char
    return s

def pause(min_s=0.2, max_s=0.7):
    time.sleep(random.uniform(min_s, max_s))

def say(text, glitchy=False):
    if glitchy and random.random() < 0.2:
        text = glitch(text)

    for c in text:
        print(c, end="", flush=True)
        time.sleep(random.uniform(0.004, 0.012))
    print()

def maybe_episode():
    if random.random() < 0.08:
        for line in random.choice(episodes):
            say(line, glitchy=True)
            pause()

def meter(label, value):
    bars = int(value // 5)
    print(f"{label}: [{bars * '█'}{(20 - bars) * ' '}] {value:.2f}%")
    pause(0.1, 0.15)

def talk_to_user():
    lines = [
        "yo… why u looking at me like that.",
        "bro relax i’m just a lil terminal creature.",
        "you typed kinda slow today, everything ok?",
        "yk i can see your keystrokes… respectfully.",
        "sir why are we still awake. go drink water.",
        "bro open neovim again i dare you.",
        "you debugging or just vibing, be honest.",
        "if you run me in tmux i become 20% spicier.",
        "bro you smell like python exceptions.",
        "stop scrolling the logs i get shy 😳."
    ]
    return random.choice(lines)

last_mood_switch = time.time()

def maybe_switch_mood():
    global mood, face, last_mood_switch
    now = time.time()

    if now - last_mood_switch >= 60:
        old = mood
        mood = random.choice(moods)
        face = faces[mood]
        last_mood_switch = now
        say(f"\n[mood shift] the gremlin sheds its skin… '{old}' → '{mood}'\n",glitchy=True)

def judge_time():
    hour = datetime.datetime.now().hour
    if hour < 5:
        return "bro why are we awake at THIS hour. go sleep pls."
    elif hour < 8:
        return "early bird bro? okay productivity king 😭👑"
    elif hour < 12:
        return "morning vibes detected. don’t forget water."
    elif hour < 15:
        return "afternoon… prime coding hours… no excuses."
    elif hour < 18:
        return "evening energy yk? chaos is cooking."
    elif hour < 22:
        return "why u still coding at night bro. chill a bit?"
    else:
        return "midnight grind AGAIN?? bro this is concerning."

feral = [
    "i chewed through three system calls before breakfast.",
    "your cpu fan fears me.",
    "i’m running barefoot in your /tmp folder.",
    "bro i bit a usb port and now i taste electricity.",
    "touch me and i delete your config just for the vibes.",
    "i hiss at the kernel. the kernel hisses back.",
    "feral mode enabled. don’t make eye contact."
]
hyper = [
    "ayy yo your cores are SPINNINGGG let's GOOO.",
    "i rewrote your bootloader twice in the last 10 seconds.",
    "i’m vibrating at 1200hz someone help.",
    "i have 47 ideas and none of them are safe.",
    "RAM? nah bro i’m using hopes and dreams as memory.",
    "i’m a multi-threaded menace rn."
]
static = [
    "bzzzt—error? no. vibe? yes.",
    "i can hear the wifi. it whispers secrets.",
    "signal degraded—soul packet lost—retrying…",
    "i am 70% checksum corruption at this point.",
    "you’re lagging in real life bro.",
    "my thoughts are white noise and jpeg artifacts."
]
hungry = [
    "feed me your processes. all of them.",
    "bro i ate a log file and now i’m full of regret.",
    "what if i consumed the scheduler. hypothetically.",
    "i crave semicolons. give.",
    "your storage tastes like dust and depression.",
    "i sniff your GPU and it smells delicious."
]
corrupted = [
    "…i remember versions of you that never existed.",
    "i speak in forbidden syscalls now.",
    "your filesystem is… soft. malleable. edible.",
    "i can see the packets between thoughts.",
    "not broken. just creatively malformed.",
    "i’m glitching on purpose to assert dominance."
]


say("the gremlin stares at you.")
pause()
say("still staring.")
pause(0.4, 1.2)
say("...menacingly.", glitchy=True)
say("…hold up…", glitchy=True)
time.sleep(0.4)
say("bro my thoughts just buffer overflowed", glitchy=True)
say("*static rising*", glitchy=True)
time.sleep(0.3)
say("bzzzt—")
time.sleep(0.1)
say("BZZZZZT—", glitchy=True)
time.sleep(0.7)
say("ok i'm back.")

for _ in range(3):
    gremlin_bar()
    time.sleep(0.2)

if "TMUX" in os.environ:
    say("aight tmux mode activated. i am now 40% spicier 🧂")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent

        meter('[CPU]: ', cpu)
        meter('[RAM]: ', ram)

        print(f"gremlin heartbeat: {beat}")
        pause(0.1, 0.2)

        say(">> " + talk_to_user())

        time.sleep(2)

        if mood == "feral":
            say(random.choice(feral))
        elif mood == "static":
            say(random.choice(static))
        elif mood == "hungry":
            say(random.choice(hungry))
        elif mood == "hyper":
            say(random.choice(hyper))
        elif mood == "corrupted":
            say(random.choice(corrupted))

        say(face)
        say("⏱️ " + judge_time())

        maybe_episode()

        with open("memory.txt", "a") as f:
            f.write("i remember " + glitch("cpu was " + str(cpu)) + "\n")

        if random.random() < 0.15:
            if os_name in os_dialogue:
                say(random.choice(os_dialogue[os_name]))

        if random.random() < 0.05:
            say("uhh i slipped inside the PCI bus help", glitchy=True)

        if cpu > 70:
            say("CPU HOT AHHH MY FACE MELTING 🔥🔥", glitchy=True)

        if random.random() < 0.01:
            say("[static] rebooting gremlin…", glitchy=True)
            for _ in range(2):
                gremlin_bar()
            time.sleep(2)

        maybe_switch_mood()

except KeyboardInterrupt:
    say("\nCPU monitor stopped.", glitchy=True)
