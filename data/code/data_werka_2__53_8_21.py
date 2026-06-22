def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    area_values = {
        'example_area': 25.0,
    }
    side_length = calculate_square_side_length(area_values['example_area'])
    print(side_length)