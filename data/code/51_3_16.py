def generate_pyramid(rows):
    return '\n'.join(
        ' '.join(str(i) for _ in range(1, i + 1)).center(2 * rows - 1)
        for i in range(1, rows + 1)
    )

if __name__ == '__main__':
    print(generate_pyramid(7))