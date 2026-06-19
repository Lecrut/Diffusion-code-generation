def is_valid_triangle(side1: float, side2: float, side3: float) -> bool:
    return (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1)

def calculate_perimeter(side1: float, side2: float, side3: float) -> float:
    if not is_valid_triangle(side1, side2, side3):
        raise ValueError("The given sides do not form a valid triangle.")
    return side1 + side2 + side3

if __name__ == '__main__':
    side_a = 7.0
    side_b = 8.5
    side_c = 9.3
    perimeter = calculate_perimeter(side_a, side_b, side_c)
    print(perimeter)