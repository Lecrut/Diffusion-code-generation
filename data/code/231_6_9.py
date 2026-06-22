def generate_repeating_pattern(word, count):
    return ' '.join([word] * count)

if __name__ == '__main__':
    result = generate_repeating_pattern('hello', 10)
    print(result)