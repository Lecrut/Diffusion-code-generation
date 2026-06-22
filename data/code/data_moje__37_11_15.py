def compute_parallelogram_area(base: float, height: float) -> float:
    surface = base * height
    return surface

if __name__ == '__main__':
    base_dimension = 7.5
    height_dimension = 4.2
    calculated_area = compute_parallelogram_area(base_dimension, height_dimension)
    print(calculated_area)