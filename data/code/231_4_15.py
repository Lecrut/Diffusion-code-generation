def generate_pattern(length):
    pattern = [0, 1]
    result = []
    for i in range(length):
        result.append(pattern[i % len(pattern)])
    return result

if __name__ == '__main__':
    sample_length = 50
    print(generate_pattern(sample_length))