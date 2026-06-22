def print_filled_rectangle(width, height, symbol):
    row = symbol * width
    rectangle = '\n'.join([row] * height)
    return rectangle

if __name__ == '__main__':
    sample_width = 10
    sample_height = 5
    sample_symbol = '*'
    print(print_filled_rectangle(sample_width, sample_height, sample_symbol))