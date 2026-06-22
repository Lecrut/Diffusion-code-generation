def generate_pattern(length):
    return [i % 2 for i in range(length)]

if __name__ == '__main__':
    pattern_length = 50
    result = generate_pattern(pattern_length)
    print(result)