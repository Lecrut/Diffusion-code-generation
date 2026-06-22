import itertools

def generate_sequence(m):
    return list(enumerate(itertools.cycle('XY'))[:m])

if __name__ == '__main__':
    sample_output = generate_sequence(5)
    print(sample_output)