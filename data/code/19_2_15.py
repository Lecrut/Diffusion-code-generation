import random

def pick_random_character(s):
    if not s:
        raise ValueError("String cannot be empty")
    index = random.randint(0, len(s) - 1)
    return s[index]

if __name__ == '__main__':
    sample_string = "HelloWorld"
    result = pick_random_character(sample_string)
    print(result)