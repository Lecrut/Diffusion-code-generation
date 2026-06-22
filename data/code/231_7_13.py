import numpy as np

def generate_pattern(length):
    if length <= 0:
        raise ValueError("Length must be greater than zero")
    return [True, False] * (length // 2) + ([True] if length % 2 != 0 else [])

if __name__ == '__main__':
    pattern = generate_pattern(25)
    print("Repeating sequence:")
    for i in range(0, len(pattern), 5):
        print(pattern[i:i+5])