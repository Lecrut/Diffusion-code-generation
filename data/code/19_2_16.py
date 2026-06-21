import random

def pick_random_character(text):
    if not text:
        return None
    index = random.randrange(len(text))
    return text[index]

if __name__ == '__main__':
    result = pick_random_character("hello")
    print(result)