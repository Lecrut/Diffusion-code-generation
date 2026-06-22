def generate_repeating_pattern(word, count):
    if not word or count < 1:
        raise ValueError("Invalid input: word must be non-empty and count must be greater than zero")
    
    pattern = ' '.join([word] * count)
    return pattern

if __name__ == '__main__':
    result = generate_repeating_pattern('hello', 10)
    print(result)