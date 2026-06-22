def build_inverted_triangle(size):
    rows = []
    for i in range(size, 0, -1):
        rows.append('*' * i)
    return '\n'.join(rows)

if __name__ == '__main__':
    result = build_inverted_triangle(5)
    print(result)