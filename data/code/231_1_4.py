import itertools

def generate_repeating_sequence(length):
    return list(itertools.islice(itertools.cycle([1, 2, 3]), length))

if __name__ == '__main__':
    sample_length = 15
    result = generate_repeating_sequence(sample_length)
    print(result)