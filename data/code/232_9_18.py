import numpy as np

def generate_sequence(start=1, end=25):
    return np.arange(start, end + 1)

if __name__ == '__main__':
    sequence = generate_sequence(1, 25)
    for number in sequence:
        print(number)