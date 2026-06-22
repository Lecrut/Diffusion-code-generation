import itertools

def validate_input(m):
    if not isinstance(m, int) or m <= 0:
        raise ValueError("Input must be a positive integer")

def generate_sequence(m):
    validate_input(m)
    return list(enumerate(itertools.cycle('XY'), start=1))[:m]

if __name__ == '__main__':
    sample_output = generate_sequence(5)
    print(sample_output)