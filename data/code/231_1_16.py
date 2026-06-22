import itertools

def generate_repeating_sequence(length):
    pattern = [1, 2, 3]
    return list(itertools.islice(itertools.cycle(pattern), length))

if __name__ == '__main__':
    sample_length = 15
    generated_sequence = generate_repeating_sequence(sample_length)
    print(generated_sequence)