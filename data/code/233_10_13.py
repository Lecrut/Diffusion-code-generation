CHAR_WIDTH = 10
CHAR_HEIGHT = 5
FILL_SYMBOL = "*"

def fill_rectangle(width=CHAR_WIDTH, height=CHAR_HEIGHT, symbol=FILL_SYMBOL):
    return [symbol * width for _ in range(height)]

if __name__ == '__main__':
    rectangle = fill_rectangle()
    for row in rectangle:
        print(row)