def calculate_area_difference(area1, area2):
    if not isinstance(area1, (int, float)) or not isinstance(area2, (int, float)):
        raise ValueError("Both areas must be integers or floats.")
    
    difference = abs(area1 - area2)
    return difference

if __name__ == '__main__':
    sample_area_one = 75.3
    sample_area_two = 42.8
    result_difference = calculate_area_difference(sample_area_one, sample_area_two)
    print(result_difference)