import itertools

def generate_sequence(m):
    return list(enumerate(itertools.cycle('XY'))[:m])

if __name__ == '__main__':
    result = generate_sequence(10)
    print(result)