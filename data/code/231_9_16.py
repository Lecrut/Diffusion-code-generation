def generate_pattern(length):
    pattern = 'abcde'
    repeated_pattern = (pattern * ((length // len(pattern)) + 1))[:length]
    return repeated_pattern

if __name__ == '__main__':
    sample_length = 50
    result = generate_pattern(sample_length)
    print(result)