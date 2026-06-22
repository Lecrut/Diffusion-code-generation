def generate_asterisk_pattern(size):
    return '\n'.join(['* ' * size for _ in range(size)])

if __name__ == '__main__':
    pattern = generate_asterisk_pattern(10)
    print(pattern)