def fill_rectangle(width, height, symbol):
    for y in range(height):
        for x in range(width):
            print(symbol, end="")
        print()
if __name__ == '__main__':
    W = 10
    H = 5
    S = "*"
    fill_rectangle(W, H, S)