import numpy as np

def validate_range(start, end):
    if start <= 0 or end < start:
        raise ValueError("Start must be greater than 0 and end must be greater than or equal to start")

def generate_sequence(start, end):
    validate_range(start, end)
    return np.arange(start, end + 1)

if __name__ == '__main__':
    start_value = 1
    end_value = 25
    sequence = generate_sequence(start_value, end_value)
    print(sequence)