PATTERN_LENGTH = 2

def generate_pattern(length):
    return [i % PATTERN_LENGTH for i in range(length)]

if __name__ == '__main__':
    sample_length = 50
    pattern = generate_pattern(sample_length)
    print(pattern)