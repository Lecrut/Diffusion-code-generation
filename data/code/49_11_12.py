def generate_square_pattern(size=10):
    return ['* ' * size for _ in range(size)]

def print_square_pattern(pattern):
    for row in pattern:
        print(row)

if __name__ == '__main__':
    size = 10
    pattern = generate_square_pattern(size)
    print_square_pattern(pattern)