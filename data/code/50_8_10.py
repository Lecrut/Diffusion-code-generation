def print_star_pyramid():
    base_width = 21
    stars = base_width // 2
    for i in range(stars + 1):
        spaces = " " * (stars - i)
        stars_count = 2 * i + 1
        line = spaces + "*" * stars_count
        print(line)

if __name__ == '__main__':
    print_star_pyramid()