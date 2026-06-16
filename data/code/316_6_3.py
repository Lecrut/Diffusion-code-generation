def print_grid(width, height, char):
    for y in range(height):
        for x in range(width):
            print(char, end="")
            if x < width - 1:
                print(" ", end="")
        print()
if __name__ == '__main__':
    grid_width = 10
    grid_height = 5
    character = '#'
    print_grid(grid_width, grid_height, character)