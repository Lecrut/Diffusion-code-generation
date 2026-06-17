def print_grid(width, height, char):
    for y in range(height):
        for x in range(width):
            print(char, end="")
        print()
if __name__ == '__main__':
    width = 10
    height = 5
    char = '#'
    print_grid(width, height, char)