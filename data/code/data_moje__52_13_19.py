def print_diamond_pattern(height: int) -> None:
    if height <= 0:
        return
    top_half = [f"{' ' * (height - i)}{'*' * (2 * i - 1)}" for i in range(1, height + 1)]
    bottom_half = [line for line in reversed(top_half[:-1])]
    all_lines = top_half + bottom_half
    for line in all_lines:
        print(line)

if __name__ == '__main__':
    sample_height = 5
    print_diamond_pattern(sample_height)