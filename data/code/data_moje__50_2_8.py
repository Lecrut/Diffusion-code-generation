def generate_centered_triangle(levels):
    max_width = 2 * levels - 1
    return '\n'.join(
        ' ' * (levels - i) + '* ' * i
        for i in range(1, levels + 1)
    )

if __name__ == '__main__':
    print(generate_centered_triangle(12))