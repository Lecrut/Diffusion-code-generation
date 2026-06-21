import random

def pick_random_character(text):
    if not text:
        return None
    index = random.randint(0, len(text) - 1)
    return text[index]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = pick_random_character(sample_string)
    print(result)