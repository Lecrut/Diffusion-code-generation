def surface_area(length: float, width: float, height: float) -> float:
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    l = 5.0
    w = 3.0
    h = 4.0
    print(surface_area(l, w, h))