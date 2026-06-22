SYMBOL = "+"
WIDTH = 10
HEIGHT = 10

def create_grid(symbol, width, height):
    row = symbol * width + "\n"
    grid = (row * height).rstrip('\n')
    return grid

if __name__ == '__main__':
    result = create_grid(SYMBOL, WIDTH, HEIGHT)
    print(result)