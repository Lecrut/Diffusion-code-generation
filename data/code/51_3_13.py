def generate_pyramid(rows=7):
    lines = [
        ' ' * (rows - i) + ' '.join(str(i) for _ in range(2 * i - 1))
        for i in range(1, rows + 1)
    ]
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_pyramid())