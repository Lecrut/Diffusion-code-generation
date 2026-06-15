def create_rectangle(symbol, width, height):
    rect = ""
    for _ in range(height):
        rect += symbol * width + "\n"
    return rect.rstrip('\n')
if __name__ == '__main__':
    symbol_val = "#"
    width_val = 10
    height_val = 3
    result = create_rectangle(symbol_val, width_val, height_val)
    print(result)