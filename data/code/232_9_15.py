import numpy as np

def generate_sequence(start=1, end=25):
    if start < 1 or end > 25:
        raise ValueError("Start and end must be between 1 and 25 inclusive.")
    return np.arange(start, end + 1)

if __name__ == '__main__':
    try:
        sequence = generate_sequence()
        print(sequence)
    except ValueError as e:
        print(e)