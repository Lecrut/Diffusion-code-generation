def calculate_perimeter(side1: float, side2: float, side3: float) -> float:
    return side1 + side2 + side3

if __name__ == '__main__':
    first_side = 6.5
    second_side = 7.8
    third_side = 9.0
    perimeter_value = calculate_perimeter(first_side, second_side, third_side)
    print(perimeter_value)