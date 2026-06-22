def surface_area_of_rectangular_box(length: float, width: float, height: float) -> float:
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    l = 1.5
    w = 2.5
    h = 3.5
    result = surface_area_of_rectangular_box(l, w, h)
    print(result)