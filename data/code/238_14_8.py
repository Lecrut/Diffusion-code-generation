def create_box(symbol, height, width):
    return symbol * width + '\n' * (height - 1) + symbol * width

if __name__ == '__main__':
    box = create_box('@', 3, 2)
    print(box)