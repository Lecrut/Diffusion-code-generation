def generate_pattern(length):
    if length <= 0:
        raise ValueError("Length must be greater than 0")
    
    pattern = [i % 2 for i in range(length)]
    return pattern

if __name__ == '__main__':
    sample_length = 50
    try:
        result = generate_pattern(sample_length)
        print(result)
    except ValueError as e:
        print(e)