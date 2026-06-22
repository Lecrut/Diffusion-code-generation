def generate_pattern(length):
    if not isinstance(length, int) or length < 1:
        raise ValueError("Length must be a positive integer")
    
    pattern = ''.join(['AB' for _ in range((length + 1) // 2)])
    if length % 2 != 0:
        pattern += 'A'
    
    return pattern

if __name__ == '__main__':
    sample_length = 20
    result = generate_pattern(sample_length)
    print(result)