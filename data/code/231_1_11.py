import itertools

PATTERN = [1, 2, 3]
LENGTH = 15

def generate_sequence():
    return list(itertools.islice(itertools.cycle(PATTERN), LENGTH))

if __name__ == '__main__':
    sequence = generate_sequence()
    print(sequence)