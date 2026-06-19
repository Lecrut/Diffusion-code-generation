def calculate_area_difference(area1, area2):
    try:
        if not isinstance(area1, (int, float)) or not isinstance(area2, (int, float)):
            raise ValueError("Both inputs must be numbers.")
        return abs(area1 - area2)
    except ValueError as e:
        print(e)
        return None

if __name__ == '__main__':
    sample_area_a = 100
    sample_area_b = 45
    result = calculate_area_difference(sample_area_a, sample_area_b)
    if result is not None:
        print(result)