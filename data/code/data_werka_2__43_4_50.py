def calculate_square_area(side_length: float) -> float:
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_values = {
        "small": 2.0,
        "medium": 4.5,
        "large": 6.7
    }
    for size, value in sample_values.items():
        area = calculate_square_area(value)
        print(f"The area of a square with side length {value} is {area:.2f}")