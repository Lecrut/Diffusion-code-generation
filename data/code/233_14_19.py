def print_filled_rectangle(width, height, symbol):
    for _ in range(height):
        print(symbol * width)

if __name__ == '__main__':
    print_filled_rectangle(5, 3, '*')