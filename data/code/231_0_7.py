def generate_pattern(length=20):
    pattern = ''.join(['AB' for _ in range(length // 2)])
    return pattern

if __name__ == '__main__':
    sample_length = 20
    result = generate_pattern(sample_length)
    print(result)