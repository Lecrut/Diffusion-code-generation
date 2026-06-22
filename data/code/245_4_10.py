def calculate_parallelogram_area(base: float, height: float) -> float:
    return base * height

def calculate_trapezoid_area(base1: float, base2: float, height: float) -> float:
    return 0.5 * (base1 + base2) * height

def compare_areas(parallelogram_base: float, parallelogram_height: float,
                  trapezoid_base1: float, trapezoid_base2: float, trapezoid_height: float) -> str:
    try:
        parallelogram_area = calculate_parallelogram_area(parallelogram_base, parallelogram_height)
        trapezoid_area = calculate_trapezoid_area(trapezoid_base1, trapezoid_base2, trapezoid_height)

        if parallelogram_area == trapezoid_area:
            return "The areas are equal."
        else:
            return f"The areas are not equal. Parallelogram area: {parallelogram_area}, Trapezoid area: {trapezoid_area}"
    except TypeError as e:
        return str(e)

if __name__ == '__main__':
    print(compare_areas(10, 5, 8, 2, 10))