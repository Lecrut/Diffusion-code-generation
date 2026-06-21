from typing import Union

def calculate_triangle_perimeter(side1: float, side2: float, side3: float) -> float:
    sides = {'side1': side1, 'side2': side2, 'side3': side3}
    for side_name, length in sides.items():
        if length < 0:
            raise ValueError(f"{side_name} cannot be negative.")
    return sum(sides.values())

if __name__ == '__main__':
    try:
        perimeter = calculate_triangle_perimeter(5.5, 6.5, 7.5)
        print(perimeter)
    except ValueError as e:
        print(e)