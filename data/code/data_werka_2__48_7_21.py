def calculate_area(base, height):
    dimensions = {'base': base, 'height': height}
    for key, value in dimensions.items():
        if value <= 0:
            raise ValueError(f"{key} must be a positive number.")
    return base * height

if __name__ == '__main__':
    sample_values = {'base': 7.8, 'height': 4.6}
    area = calculate_area(**sample_values)
    print(area)