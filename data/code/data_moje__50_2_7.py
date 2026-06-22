def generate_centered_triangle(levels):
    return [
        (' ' * (levels - i - 1)) + ('*' * (2 * i + 1))
        for i in range(levels)
    ]

if __name__ == '__main__':
    levels = 12
    for line in generate_centered_triangle(levels):
        print(line)