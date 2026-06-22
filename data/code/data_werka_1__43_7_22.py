def calculate_square_area(side: float) -> float:
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side * side

if __name__ == '__main__':
    sample_values = [3.5, 7.2, 10.0]
    for value in sample_values:
        try:
            area = calculate_square_area(value)
            print(f"The area of the square with side {value} is {area}")
        except ValueError as e:
            print(e)