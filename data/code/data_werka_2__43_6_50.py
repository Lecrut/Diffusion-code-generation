def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length ** 2

if __name__ == '__main__':
    sample_values = [4, 6.2, -3, 0]
    results = {}
    for value in sample_values:
        try:
            area = calculate_square_area(value)
            results[value] = area
        except ValueError as e:
            results[value] = str(e)
    
    for side_length, result in results.items():
        print(f"The area of a square with side length {side_length} is {result}")