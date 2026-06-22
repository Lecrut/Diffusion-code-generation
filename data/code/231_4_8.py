def generate_pattern(length):
    pattern = []
    for i in range(length):
        pattern.append(i % 2)
    return pattern

if __name__ == '__main__':
    sample_length = 50
    print(generate_pattern(sample_length))