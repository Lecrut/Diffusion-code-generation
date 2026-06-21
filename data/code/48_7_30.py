def calculate_area(base, height):
    dimensions = {'base': base, 'height': height}
    for key, value in dimensions.items():
        if not isinstance(value, (int, float)):
            raise TypeError(f"{key} must be a number.")
        if value <= 0:
            raise ValueError(f"{key} must be a positive number.")
    return base * height

if __name__ == '__main__':
    sample_values = {'base': 9.1, 'height': 5.4}
    area = calculate_area(**sample_values)
    print(area)