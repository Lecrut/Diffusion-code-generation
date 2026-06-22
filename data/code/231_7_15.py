import numpy as np

def generate_boolean_pattern(n):
    return np.array([True, False] * (n // 2 + n % 2))

if __name__ == '__main__':
    pattern = generate_boolean_pattern(25)
    print("Repeating boolean pattern:")
    for i in range(0, len(pattern), 10):
        print(pattern[i:i+10])