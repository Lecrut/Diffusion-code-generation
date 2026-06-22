def surface_area_box(length: float, width: float, height: float) -> float:
    if length <= 0 or width <= 0 or height <= 0:
        return 0.0
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    l = 5.0
    w = 3.0
    h = 4.0
    result = surface_area_box(l, w, h)
    print(result)