def generate_reverse_triangle(rows=5):
    lines = [
        ' '.join(str(j) for j in range(i, 0, -1))
        for i in range(rows, 0, -1)
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_reverse_triangle())