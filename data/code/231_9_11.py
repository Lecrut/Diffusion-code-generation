def generate_pattern(length):
    if length <= 0:
        raise ValueError("Length must be greater than zero")
    
    pattern = 'abcde' * (length // 5 + 1)
    return pattern[:length]

if __name__ == '__main__':
    result = generate_pattern(50)
    print(result)