from typing import Union

def calculate_triangle_perimeter(side_a: Union[int, float], side_b: Union[int, float], side_c: Union[int, float]) -> float:
    if any(side <= 0 for side in [side_a, side_b, side_c]):
        raise ValueError("All sides must be positive numbers.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(3.0, 4.0, 5.0)
        print(f"Side A: 3.0")
        print(f"Side B: 4.0")
        print(f"Side C: 5.0")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")