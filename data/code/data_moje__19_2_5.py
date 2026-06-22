import random

def pick_random_char(s: str) -> str:
    index = random.randint(0, len(s) - 1)
    return s[index]

if __name__ == '__main__':
    test_string = "example"
    result = pick_random_char(test_string)
    print(result)