def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    test_cases = {
        'small': 16,
        'medium': 25,
        'large': 81
    }
    for description, area in test_cases.items():
        side_length = calculate_square_side_length(area)
        print(f"The side length of the {description} square is: {side_length}")