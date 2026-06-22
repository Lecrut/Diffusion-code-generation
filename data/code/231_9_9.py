def generate_pattern(length):
    pattern = 'abcde'
    return (pattern * (length // len(pattern) + 1))[:length]

if __name__ == '__main__':
    sample_length = 50
    result = generate_pattern(sample_length)
    print(result)