import itertools

def generate_sequence(m):
    if not isinstance(m, int) or m <= 0:
        raise ValueError("Input must be a positive integer")
    return list(enumerate(itertools.cycle('XY'), start=1))[:m]

if __name__ == '__main__':
    sample_output = generate_sequence(5)
    print(sample_output)