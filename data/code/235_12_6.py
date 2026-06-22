def generate_pyramid_line(n):
    return '\n'.join('*' * i for i in range(1, n + 1))

if __name__ == '__main__':
    sample_number = 5
    print(generate_pyramid_line(sample_number))