def generate_pattern(length):
    if length < 1:
        raise ValueError("Length must be at least 1")
    
    pattern = 'abcde' * (length // 5)
    remainder = length % 5
    if remainder > 0:
        pattern += 'abcde'[:remainder]
    
    return pattern

if __name__ == '__main__':
    sample_length = 50
    result = generate_pattern(sample_length)
    print(result)