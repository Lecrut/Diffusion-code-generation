def generate_pattern(length):
    if length <= 0:
        raise ValueError("Length must be greater than zero")
    
    pattern = []
    for i in range(length):
        pattern.append(i % 2)
    
    return pattern

if __name__ == '__main__':
    sample_length = 50
    result = generate_pattern(sample_length)
    print(result)