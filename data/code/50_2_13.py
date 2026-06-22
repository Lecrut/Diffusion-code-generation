def print_centered_triangle(levels: int) -> None:
    [print(' ' * (levels - i) + '*' * (2 * i - 1)) for i in range(1, levels + 1)]

if __name__ == '__main__':
    sample_levels = 12
    print_centered_triangle(sample_levels)