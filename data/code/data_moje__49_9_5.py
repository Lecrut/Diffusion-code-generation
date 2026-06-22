def generate_star_pattern(size):
    row = '*' * size
    lines = [row for _ in range(size)]
    return '\n'.join(lines)

if __name__ == '__main__':
    SIZE = 12
    result = generate_star_pattern(SIZE)
    print(result)