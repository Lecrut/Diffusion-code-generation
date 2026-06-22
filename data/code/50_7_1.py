def generate_triangle(height=20):
    rows = []
    for i in range(1, height + 1):
        rows.append('*' * i)
    return '\n'.join(rows)

if __name__ == '__main__':
    height = 20
    result = generate_triangle(height)
    print(result)