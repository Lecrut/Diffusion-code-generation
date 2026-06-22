def generate_asterisk_square(size=10):
    return ['* ' * size for _ in range(size)]

if __name__ == '__main__':
    pattern = generate_asterisk_square()
    for line in pattern:
        print(line)