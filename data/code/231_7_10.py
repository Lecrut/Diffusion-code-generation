import numpy as np

def generate_pattern(n):
    return [True, False] * (n // 2)

if __name__ == '__main__':
    pattern = generate_pattern(25)
    print("Generated pattern:", pattern)
    
    another_pattern = generate_pattern(18)
    print("Another generated pattern:", another_pattern)