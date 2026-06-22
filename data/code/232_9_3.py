import numpy as np

def generate_sequence(start, end):
    return np.arange(start, end + 1)

if __name__ == '__main__':
    start_value = 5
    end_value = 20
    sequence = generate_sequence(start_value, end_value)
    print(sequence)