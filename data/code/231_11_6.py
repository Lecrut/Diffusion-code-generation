import itertools

def generate_sequence(m):
    if not isinstance(m, int) or m <= 0:
        raise ValueError("Input must be a positive integer.")
    
    sequence = list(enumerate(itertools.cycle('XY'), start=1))[:m]
    return sequence

if __name__ == '__main__':
    sample_output = generate_sequence(5)
    print(sample_output)