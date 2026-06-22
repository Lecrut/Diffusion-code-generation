def generate_pyramid_line(n):
    return '\n'.join('*' * (2 * i - 1) for i in range(1, n + 1))

if __name__ == '__main__':
    sample_number = 5
    pyramid_pattern = generate_pyramid_line(sample_number)
    print(pyramid_pattern)