def generate_pattern(length):
    pattern = [i % 2 for i in range(length)]
    return pattern

if __name__ == '__main__':
    length = 50
    sample_pattern = generate_pattern(length)
    print(sample_pattern)