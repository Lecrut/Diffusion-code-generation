def generate_reverse_triangle(rows=5):
    lines = [
        ' '.join(str(num) for num in range(rows - i, 0, -1))
        for i in range(rows)
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    result = generate_reverse_triangle(5)
    print(result)