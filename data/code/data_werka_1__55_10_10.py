from typing import Union

def calculate_triangle_perimeter(side_a: Union[int, float], side_b: Union[int, float], side_c: Union[int, float]) -> float:
    if any(side <= 0 for side in [side_a, side_b, side_c]):
        raise ValueError("All sides must be positive numbers.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    try:
        side1 = 7.5
        side2 = 9.3
        side3 = 12.1
        perimeter = calculate_triangle_perimeter(side1, side2, side3)
        print(f"Side A: {side1}")
        print(f"Side B: {side2}")
        print(f"Side C: {side3}")
        print(f"The perimeter of the triangle is: {perimeter}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")