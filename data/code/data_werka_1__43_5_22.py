def calculate_square_area(side_length: float) -> float:
    return side_length ** 2

if __name__ == '__main__':
    sample_values = {
        'side1': 3.0,
        'side2': 4.5,
        'side3': 7.2
    }
    
    for name, side in sample_values.items():
        area_result = calculate_square_area(side)
        print(f"The area of a square with side length {side} is: {area_result}")