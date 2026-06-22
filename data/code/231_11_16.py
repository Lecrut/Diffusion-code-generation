import itertools

def generate_sequence(m):
    sequence = list(itertools.cycle('XY'))
    result = [(i, char) for i, char in enumerate(sequence, start=1)]
    return result[:m]

if __name__ == '__main__':
    sample_output = generate_sequence(7)
    print(sample_output)