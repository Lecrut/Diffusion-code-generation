import numpy as np

def validate_input(start, end):
    if start < 1 or end > 25:
        raise ValueError("Start must be between 1 and 25, inclusive. End must also be between 1 and 25, inclusive.")

def generate_sequence(start, end):
    validate_input(start, end)
    return np.arange(start, end + 1)

if __name__ == '__main__':
    start_value = 1
    end_value = 25
    sequence = generate_sequence(start_value, end_value)
    print(sequence)