def generate_inverted_triangle(n: int) -> list[str]:
    return ['*' * (n - i) for i in range(n)]

if __name__ == '__main__':
    lines = generate_inverted_triangle(5)
    print('\n'.join(lines))