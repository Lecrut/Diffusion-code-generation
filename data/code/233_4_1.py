def create_rectangle(symbol, width, height):
    line = ""
    for _ in range(height):
        line += symbol * width + "\n"
    return line.rstrip('\n')
if __name__ == '__main__':
    symbol = "#"
    width = 10
    height = 5
    result = create_rectangle(symbol, width, height)
    print(result)