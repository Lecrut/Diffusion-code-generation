def calculate_area_difference(area1, area2):
    if not isinstance(area1, (int, float)) or not isinstance(area2, (int, float)):
        raise ValueError("Both areas must be integers or floats.")
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_area1 = 50.5
    sample_area2 = 30.2
    result = calculate_area_difference(sample_area1, sample_area2)
    print(result)