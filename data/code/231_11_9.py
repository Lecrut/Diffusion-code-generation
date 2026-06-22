import itertools

def generate_sequence(m):
    return list(enumerate(itertools.cycle('XY'))[:m])

if __name__ == '__main__':
    print(generate_sequence(5))