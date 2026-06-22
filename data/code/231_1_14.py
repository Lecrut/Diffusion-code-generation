import itertools

def validate_length(length):
    if not isinstance(length, int) or length < 1:
        raise ValueError("Length must be a positive integer")

def create_repeating_sequence(length):
    validate_length(length)
    pattern = [1, 2, 3]
    return list(itertools.islice(itertools.cycle(pattern), length))

if __name__ == '__main__':
    sample_length = 15
    result = create_repeating_sequence(sample_length)
    print(result)