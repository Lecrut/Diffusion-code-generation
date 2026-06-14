import sys
def draw_rectangle(width, height, symbol):
    for y in range(height):
        line = ""
        for x in range(width):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                line += "#"
            else:
                line += " "
        print(line)
if __name__ == '__main__':
    width = 10
    height = 5
    symbol = "*"
    if not isinstance(width, int) or width <= 0:
        print("Error: Width must be a positive integer.")
        sys.exit(1)
    if not isinstance(height, int) or height <= 0:
        print("Error: Height must be a positive integer.")
        sys.exit(1)
    if not isinstance(symbol, str) or len(symbol) != 1:
        print("Error: Symbol must be a single character.")
        sys.exit(1)
    print(f"Drawing rectangle of size {width}x{height} with symbol '{symbol}':")
    for y in range(height):
        line = ""
        for x in range(width):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                line += "#"
            else:
                line += " "
        print(line)