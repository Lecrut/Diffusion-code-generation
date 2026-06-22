import numpy as np

def generate_pattern():
    if np:
        pattern = np.array([True, False] * 13)
    else:
        pattern = [True, False] * 13
    return pattern[:25]

if __name__ == '__main__':
    print(generate_pattern())