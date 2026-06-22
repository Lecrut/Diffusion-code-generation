import itertools
PATTERN = [1, 2, 3]

def create_repeating_sequence(length):
    return list(itertools.islice(itertools.cycle(PATTERN), length))
if __name__ == '__main__':
    sample_length = 15
    result = create_repeating_sequence(sample_length)
    print(result)