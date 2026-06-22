from typing import Union

def calculate_triangle_perimeter(side_a: float, side_b: float, side_c: float) -> Union[float, str]:
    try:
        if not (side_a > 0 and side_b > 0 and side_c > 0):
            raise ValueError("All sides must be positive numbers.")
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("The sum of any two sides must be greater than the third side.")
        return side_a + side_b + side_c
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    sample_sides = (3.0, 4.0, 5.0)
    perimeter = calculate_triangle_perimeter(*sample_sides)
    print(perimeter)