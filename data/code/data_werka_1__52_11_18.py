def calculate_area(x1, y1):
    def validate_coordinates(x, y):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise ValueError("Coordinates must be numeric.")
    
    validate_coordinates(x1, y1)
    area = abs(0.5 * (x1 * 0 + y1 * 0 - 0 * y1 - 0 * x1))
    return area

if __name__ == '__main__':
    sample_x = 6.0
    sample_y = 8.0
    result = calculate_area(sample_x, sample_y)
    print(result)