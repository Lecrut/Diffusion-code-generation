def calculate_parallelogram_area(base: float, height: float) -> float:
    return base * height

def calculate_trapezoid_area(base1: float, base2: float, height: float) -> float:
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    parallelogram_base = 10.0
    parallelogram_height = 5.0
    trapezoid_base1 = 8.0
    trapezoid_base2 = 6.0
    trapezoid_height = 4.0

    parallelogram_area = calculate_parallelogram_area(parallelogram_base, parallelogram_height)
    trapezoid_area = calculate_trapezoid_area(trapezoid_base1, trapezoid_base2, trapezoid_height)

    print(f"Parallelogram area: {parallelogram_area}")
    print(f"Trapezoid area: {trapezoid_area}")

    if parallelogram_area == trapezoid_area:
        print("The areas are equal.")
    else:
        print("The areas are not equal.")