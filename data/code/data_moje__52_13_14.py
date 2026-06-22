def print_diamond_star_pattern(height: int) -> None:
    if height % 2 == 0 or height < 1:
        return

    mid = height // 2
    upper_rows = [f"{' ' * (mid - i)}{'*' * (2 * i + 1)}" for i in range(mid + 1)]
    lower_rows = [f"{' ' * (mid - i)}{'*' * (2 * i + 1)}" for i in range(mid - 1, -1, -1)]
    diamond = upper_rows + lower_rows

    for line in diamond:
        print(line)

if __name__ == '__main__':
    sample_height = 7
    print_diamond_star_pattern(sample_height)