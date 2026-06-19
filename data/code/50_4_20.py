def calculate_area_difference(area1_str, area2_str):
    try:
        area1 = float(area1_str)
        area2 = float(area2_str)
        return abs(area1 - area2)
    except ValueError:
        return "Invalid input: Please enter numeric values for areas."

if __name__ == '__main__':
    sample_area1 = "50.5"
    sample_area2 = "30.2"
    result = calculate_area_difference(sample_area1, sample_area2)
    print(result)