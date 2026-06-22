import numpy as np

def generate_pattern():
    return np.tile([True, False], 25)

if __name__ == '__main__':
    pattern = generate_pattern()
    print(pattern)