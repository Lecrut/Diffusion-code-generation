def print_diamond_pattern(height: int) -> None:
    if height < 1:
        return
    
    for i in range(height):
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        print(f"{spaces}{stars}")
    
    for i in range(height - 2, -1, -1):
        spaces = " " * (height - i - 1)
        stars = "*" * (2 * i + 1)
        print(f"{spaces}{stars}")

if __name__ == '__main__':
    sample_height = 5
    print_diamond_pattern(sample_height)