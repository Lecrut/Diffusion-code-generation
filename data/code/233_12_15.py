import numpy as np

def create_rectangle(width, height, symbol):
    if not (isinstance(width, int) and isinstance(height, int) and width > 0 and height > 0):
        raise ValueError("Width and height must be positive integers.")
    if not isinstance(symbol, str) or len(symbol) != 1:
        raise ValueError("Symbol must be a single character string.")
    
    rectangle = np.full((height, width), symbol)
    return rectangle

if __name__ == '__main__':
    rect1 = create_rectangle(5, 3, '*')
    print(rect1)
    print("-" * 10)
    rect2 = create_rectangle(8, 2, '#')
    print(rect2)
    print("-" * 10)
    rect3 = create_rectangle(4, 4, '@')
    print(rect3)