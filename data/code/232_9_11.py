import numpy as np

def generate_sequence(start=1, end=25):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end values must be integers.")
    if start < 1 or end > 25:
        raise ValueError("Start value must be between 1 and 25, inclusive. End value must also be between 1 and 25, inclusive.")
    return np.arange(start, end + 1)

if __name__ == '__main__':
    try:
        sequence = generate_sequence()
        print(sequence)
    except ValueError as e:
        print(e)