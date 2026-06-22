def print_reverse_triangle(height):
    if height < 1:
        return
    for row in range(1, height + 1):
        spaces = ' ' * (height - row)
        stars = '*' * (2 * row - 1)
        print(spaces + stars)

if __name__ == '__main__':
    sample_height = 5
    print_reverse_triangle(sample_height)