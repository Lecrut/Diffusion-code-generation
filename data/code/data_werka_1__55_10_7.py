from typing import Union

def calculate_triangle_perimeter(side_a: Union[int, float], side_b: Union[int, float], side_c: Union[int, float]) -> Union[int, float]:
    if any(side <= 0 for side in [side_a, side_b, side_c]):
        raise ValueError("Side lengths must be positive numbers.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    try:
        side_a = 3
        side_b = 4
        side_c = 5
        perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)
        print(f"Side A: {side_a}")
        print(f"Side B: {side_b}")
        print(f"Side C: {side_c}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(f"Error: {e}")