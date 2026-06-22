def print_pyramid(base_width=21):
    max_stars = base_width
    row = 1
    while row <= base_width:
        stars = '*' * row
        spaces = ' ' * ((max_stars - len(stars)) // 2)
        line = spaces + stars + spaces
        if len(line) > max_stars:
            line = line[:max_stars]
        print(line)
        row += 2

if __name__ == '__main__':
    print_pyramid()