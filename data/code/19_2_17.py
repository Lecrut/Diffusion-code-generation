import random

def pick_random_char(s):
    if not s:
        return None
    index = random.randint(0, len(s) - 1)
    return s[index]

if __name__ == '__main__':
    sample_string = "Hello, World!"
    result = pick_random_char(sample_string)
    print(result)