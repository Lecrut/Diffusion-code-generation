RECTANGLE_WIDTH = 8
RECTANGLE_HEIGHT = 4

def rectangle_area(w: float, h: float) -> float:
    if w <= 0 or h <= 0:
        return 0.0
    return w * h

if __name__ == '__main__':
    w = RECTANGLE_WIDTH
    h = RECTANGLE_HEIGHT
    print(rectangle_area(w, h))