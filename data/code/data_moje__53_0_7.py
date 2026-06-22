def generate_reverse_triangle(rows=5):
    return '\n'.join(
        ''.join(str(num) for num in range(rows - i, 0, -1))
        for i in range(rows)
    )

if __name__ == '__main__':
    result = generate_reverse_triangle(5)
    print(result)