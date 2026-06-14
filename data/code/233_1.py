import sys
def fill_rectangle(width, height, symbol):
    for _ in range(height):
        print(symbol * width)
if __name__ == '__main__':
    fill_rectangle(5, 3, '*')