def surface_area_of_rectangular_box(length: float, width: float, height: float) -> float:
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 1.5
    width = 2.5
    height = 3.5
    result = surface_area_of_rectangular_box(length, width, height)
    print(result)