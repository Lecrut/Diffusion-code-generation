def print_diamond_pattern(half_height: int) -> None:
    for i in range(1, half_height + 1):
        spaces = " " * (half_height - i)
        stars = "*" * (2 * i - 1)
        print(f"{spaces}{stars}")
    for i in range(half_height - 1, 0, -1):
        spaces = " " * (half_height - i)
        stars = "*" * (2 * i - 1)
        print(f"{spaces}{stars}")

if __name__ == '__main__':
    half_height_value = 4
    print_diamond_pattern(half_height_value)