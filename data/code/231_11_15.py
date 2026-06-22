import itertools
SEQUENCE = 'XY'

def generate_sequence(m):
    return list(enumerate(itertools.cycle(SEQUENCE), start=1))[:m]
if __name__ == '__main__':
    sample_output = generate_sequence(5)
    print(sample_output)