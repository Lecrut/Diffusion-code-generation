import random

def pick_random_char(s):
    index = random.randint(0, len(s) - 1)
    return s[index]

if __name__ == '__main__':
    sample_string = "deterministic"
    result = pick_random_char(sample_string)
    print(result)