def surface_area_rectangular_box(length: float, width: float, height: float) -> float:
    return 2 * (length * width + width * height + height * length)
if __name__ == '__main__':
    length = 5
    width = 3
    height = 4
    result = surface_area_rectangular_box(length, width, height)
    print(result)