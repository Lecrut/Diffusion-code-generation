def calculate_area_difference(area1, area2):
    def validate_area(area):
        if not isinstance(area, (int, float)):
            raise ValueError("Area must be a number")
        if area < 0:
            raise ValueError("Area cannot be negative")

    validate_area(area1)
    validate_area(area2)

    return abs(area1 - area2)

if __name__ == '__main__':
    sample_area1 = 85
    sample_area2 = 65
    difference = calculate_area_difference(sample_area1, sample_area2)
    print(difference)