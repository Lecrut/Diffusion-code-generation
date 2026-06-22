def print_diamond_star_pattern():
    max_width = 7
    half_height = (max_width + 1) // 2
    top_half = [f"{' ' * (half_height - i)}*{'*' * (2*i - 1)}" for i in range(1, half_height + 1)]
    bottom_half = top_half[-2::-1]
    diamond_pattern = top_half + bottom_half
    for line in diamond_pattern:
        print(line)

if __name__ == '__main__':
    print_diamond_star_pattern()