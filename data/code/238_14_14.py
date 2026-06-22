def create_box(symbol):
    box_template = f"{symbol * 3}\n{symbol * 3}\n"
    return box_template

if __name__ == '__main__':
    symbol = '@'
    box = create_box(symbol)
    print(box)