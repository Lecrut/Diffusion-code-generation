def generate_pyramid(n):
    return [' '.join(chr(ord('A') + abs(n - 1 - j) - (n - 1 - j)) if abs(n - 1 - j) <= n - 1 - i else '' for j in range(2 * n - 1)).strip() for i in range(n) if any(chr(ord('A') + abs(n - 1 - k) - (n - 1 - k)) if abs(n - 1 - k) <= n - 1 - i else '' for k in range(2 * n - 1)) for _ in [1]]

def print_pyramid_pattern(size):
    rows = generate_pyramid(size)
    for row in rows:
        print(row)

if __name__ == '__main__':
    print_pyramid_pattern(5)