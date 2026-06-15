def create_rectangle(symbol, width, height):
    row = ""
    for _ in range(height):
        row += symbol * width
        row += "\n"
    return row
if __name__ == '__main__':
    symbol = "#"
    width = 10
    height = 3
    result = create_rectangle(symbol, width, height)
    print(result)