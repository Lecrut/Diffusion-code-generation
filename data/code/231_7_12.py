import numpy as np

def generate_pattern(n):
    if n % 2 == 0:
        return [True, False] * (n // 2)
    else:
        return [True, False] * ((n - 1) // 2) + [True]

if __name__ == '__main__':
    pattern = generate_pattern(25)
    print(pattern)