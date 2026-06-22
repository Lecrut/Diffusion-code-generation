def generate_star_pattern(n):
    return [f"{' ' * (n - 1 - i)}{'*' * (2 * n - 1 - 2 * i)}" for i in range(n)]

if __name__ == '__main__':
    pattern = generate_star_pattern(4)
    for line in pattern:
        print(line)