def draw_rectangle(width, height):
    for y in range(height):
        for x in range(width):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                print('@', end="")
            else:
                print(' ', end="")
    print()
if __name__ == '__main__':
    draw_rectangle(10, 5)