def generate_inverted_triangle(size: int) -> str:
    if size <= 0:
        return ""
    rows = []
    for i in range(size):
        stars = '*' * (size - i)
        rows.append(stars)
    return '\n'.join(rows)

if __name__ == '__main__':
    result = generate_inverted_triangle(5)
    print(result)