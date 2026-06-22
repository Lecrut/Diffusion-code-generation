import numpy as np

def generate_pattern():
    if np:
        return np.array([True, False] * 13)
    else:
        return [True, False] * 13

if __name__ == '__main__':
    pattern = generate_pattern()
    print(pattern)