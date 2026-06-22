import itertools

def generate_sequence(m):
    pattern = list(enumerate(itertools.cycle('XY'), start=1))[:m]
    return pattern

if __name__ == '__main__':
    sample_output = generate_sequence(5)
    print(sample_output)