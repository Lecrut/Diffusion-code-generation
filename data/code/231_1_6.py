import itertools

PATTERN = [1, 2, 3]
LENGTH = 15

def create_repeating_sequence(pattern=PATTERN, length=LENGTH):
    return list(itertools.islice(itertools.cycle(pattern), length))

if __name__ == '__main__':
    sample_length = LENGTH
    result = create_repeating_sequence()
    print(result)