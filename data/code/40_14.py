def surface_area_box(l: float, w: float, h: float) -> float:
    return 2 * (l * w + w * h + h * l)

if __name__ == '__main__':
    length: float = 2.5
    width: float = 3.0
    height: float = 4.0
    result: float = surface_area_box(length, width, height)
    print(result)