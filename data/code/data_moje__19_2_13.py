import random

def pick_random_char(s: str) -> str:
    length = len(s)
    if length == 0:
        return ''
    index = random.randint(0, length - 1)
    return s[index]

if __name__ == '__main__':
    sample_string = "example"
    result = pick_random_char(sample_string)
    print(result)