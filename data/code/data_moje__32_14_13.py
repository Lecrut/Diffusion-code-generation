DEFAULT_WIDTH = 12
DEFAULT_HEIGHT = 7

def compute_rectangle_area(width=None, height=None):
    w = width if width is not None else DEFAULT_WIDTH
    h = height if height is not None else DEFAULT_HEIGHT
    return w * h

if __name__ == '__main__':
    result = compute_rectangle_area()
    print(result)