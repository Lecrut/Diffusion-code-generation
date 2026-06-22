def generate_pattern(length):
    pattern = [0, 1]
    return pattern * ((length // 2) + (length % 2))

if __name__ == '__main__':
    sample_length = 50
    print(generate_pattern(sample_length))