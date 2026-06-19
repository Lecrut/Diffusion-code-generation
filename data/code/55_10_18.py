from typing import Union

def calculate_triangle_perimeter(side_a: Union[int, float], side_b: Union[int, float], side_c: Union[int, float]) -> Union[int, float]:
    if any(side < 0 for side in (side_a, side_b, side_c)):
        raise ValueError("Side lengths must be non-negative.")
    return side_a + side_b + side_c

if __name__ == '__main__':
    sides = {
        'side_a': 5,
        'side_b': 12,
        'side_c': 13
    }
    
    try:
        perimeter = calculate_triangle_perimeter(sides['side_a'], sides['side_b'], sides['side_c'])
        print(f"Side A: {sides['side_a']}")
        print(f"Side B: {sides['side_b']}")
        print(f"Side C: {sides['side_c']}")
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")