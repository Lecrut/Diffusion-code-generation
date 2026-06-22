import random

ITEMS = {
    "red": "Ruby",
    "green": "Emerald",
    "blue": "Sapphire",
    "yellow": "Topaz"
}

def pick_random(iterable):
    return random.choice(list(iterable))

if __name__ == '__main__':
    selected = pick_random(ITEMS.values())
    print(selected)