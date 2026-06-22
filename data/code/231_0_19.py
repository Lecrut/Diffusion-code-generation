def generate_pattern(length):
    if length < 0:
        raise ValueError("Length must be non-negative")
    
    pattern = ''.join(['AB' for _ in range((length + 1) // 2)])
    return pattern[:length]

if __name__ == '__main__':
    sample_length = 20
    try:
        result = generate_pattern(sample_length)
        print(result)
    except ValueError as e:
        print(e)