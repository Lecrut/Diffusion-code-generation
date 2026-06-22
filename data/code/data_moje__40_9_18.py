def compute_surface_area(length: float, width: float, height: float) -> float:
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    print(compute_surface_area(1.5, 2.5, 3.5))