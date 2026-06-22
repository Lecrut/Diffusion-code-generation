def print_filled_rectangle(width, height, symbol):
    row = symbol * width
    rectangle = '\n'.join([row] * height)
    return rectangle

if __name__ == '__main__':
    print(print_filled_rectangle(5, 3, '*'))