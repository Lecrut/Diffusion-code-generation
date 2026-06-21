import random

def pick_random_character(s):
    length = len(s)
    if length == 0:
        return None
    index = random.randrange(length)
    return s[index]

if __name__ == '__main__':
    sample_string = "Hello World"
    result = pick_random_character(sample_string)
    print(result)