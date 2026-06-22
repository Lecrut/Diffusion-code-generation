def print_diamond_star_pattern(half_height: int) -> None:
    top_half = []
    for i in range(half_height):
        spaces = " " * (half_height - i - 1)
        stars = "*" * (2 * i + 1)
        top_half.append(spaces + stars)
    
    bottom_half = []
    for i in range(half_height - 2, -1, -1):
        spaces = " " * (half_height - i - 1)
        stars = "*" * (2 * i + 1)
        bottom_half.append(spaces + stars)
    
    full_diamond = top_half + bottom_half
    
    for line in full_diamond:
        print(line)

if __name__ == '__main__':
    print_diamond_star_pattern(4)