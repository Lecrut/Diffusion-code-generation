def display_inverted_triangle():
    height = 5
    for i in range(height):
        spaces = "  " * i
        stars = "* " * (height - i)
        print(spaces + stars.rstrip())

if __name__ == '__main__':
    display_inverted_triangle()