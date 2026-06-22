import numpy as np

def generate_pattern(iterations):
    if np:
        return np.array([True, False] * (iterations // 2))
    else:
        return [bool(i % 2 == 0) for i in range(iterations)]

if __name__ == '__main__':
    pattern = generate_pattern(25)
    print(pattern)