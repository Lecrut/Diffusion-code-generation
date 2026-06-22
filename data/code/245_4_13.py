from typing import Union

def validate_dimensions(base: Union[float, int], height: Union[float, int], side_a: Union[float, int] = None, side_b: Union[float, int] = None) -> None:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    if side_a is not None and side_b is not None and (side_a <= 0 or side_b <= 0):
        raise ValueError("Side lengths must be positive numbers.")

def calculate_parallelogram_area(base: float, height: float) -> float:
    validate_dimensions(base, height)
    return base * height

def calculate_trapezoid_area(base1: float, base2: float, height: float) -> float:
    validate_dimensions(base1, height, side_a=base2)
    return 0.5 * (base1 + base2) * height

if __name__ == '__main__':
    parallelogram_base = 5
    parallelogram_height = 3
    trapezoid_base1 = 4
    trapezoid_base2 = 6
    trapezoid_height = 2

    try:
        parallelogram_area = calculate_parallelogram_area(parallelogram_base, parallelogram_height)
        trapezoid_area = calculate_trapezoid_area(trapezoid_base1, trapezoid_base2, trapezoid_height)

        print(f"Parallelogram area: {parallelogram_area}")
        print(f"Trapezoid area: {trapezoid_area}")

        if parallelogram_area == trapezoid_area:
            print("The areas are equal.")
        else:
            print("The areas are not equal.")
    except ValueError as e:
        print(e)