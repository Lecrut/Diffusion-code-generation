def inverted_triangle(height=5):
    rows = []
    for i in range(height, 0, -1):
        rows.append('*' * i)
    return '\n'.join(rows)

if __name__ == '__main__':
    result = inverted_triangle(5)
    print(result)