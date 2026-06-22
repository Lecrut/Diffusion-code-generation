def surface_area_of_rectangular_box(length: float, width: float, height: float) -> float:
    return 2.0 * (length * width + width * height + height * length)

if __name__ == '__main__':
    result = surface_area_of_rectangular_box(1.0, 2.0, 3.0)
    print(result)