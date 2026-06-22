PATTERN = 'AB'

def generate_pattern(length):
    return ''.join([PATTERN for _ in range(length // len(PATTERN))])

if __name__ == '__main__':
    sample_length = 20
    pattern = generate_pattern(sample_length)
    print(pattern)