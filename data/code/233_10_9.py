def fill_rectangle(width, height, symbol):
    return '\n'.join([symbol * width for _ in range(height)])

if __name__ == '__main__':
    width = 10
    height = 5
    symbol = "*"
    print(fill_rectangle(width, height, symbol))