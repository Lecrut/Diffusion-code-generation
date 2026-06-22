CHAR_MAP = {'#': 1}

def generate_pyramid_line(n):
    return '\n'.join([' ' * (n - i) + '#' * (2 * i - 1) for i in range(1, n + 1)])

if __name__ == '__main__':
    sample_number = 5
    pattern = generate_pyramid_line(sample_number)
    print(pattern)