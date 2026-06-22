import numpy as np

def create_rectangle(width, height, symbol):
    array = np.full((height, width), symbol)
    return array

if __name__ == '__main__':
    rect1 = create_rectangle(5, 3, '*')
    print(rect1)
    print("-" * 10)
    rect2 = create_rectangle(8, 2, '#')
    print(rect2)
    print("-" * 10)
    rect3 = create_rectangle(4, 4, '@')
    print(rect3)