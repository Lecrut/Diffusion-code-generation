NUM_ROWS = 5

def print_inverted_pyramid():
    for i in reversed(range(1, NUM_ROWS + 1)):
        spaces = " " * (NUM_ROWS - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

if __name__ == '__main__':
    print_inverted_pyramid()