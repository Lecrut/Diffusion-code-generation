import numpy as np

def generate_sequence():
    return np.arange(1, 26)

if __name__ == '__main__':
    sequence = generate_sequence()
    print(sequence)