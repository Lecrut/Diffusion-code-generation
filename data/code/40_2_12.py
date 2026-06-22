def surface_area(length: float, width: float, height: float) -> float:
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    l, w, h = 3, 4, 5
    area = surface_area(l, w, h)
    print(area)