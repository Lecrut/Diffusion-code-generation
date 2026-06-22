import numpy as np

def validate_start_end(start, end):
    if start <= 0 or end < start:
        raise ValueError("Start must be greater than 0 and end must be greater than or equal to start")

def generate_sequence(start=1, end=25):
    validate_start_end(start, end)
    return np.arange(start, end + 1)

if __name__ == '__main__':
    sequence = generate_sequence()
    print(sequence)