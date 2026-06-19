def calculate_area_difference(area1_str, area2_str):
    try:
        area1 = float(area1_str)
        area2 = float(area2_str)
        return abs(area1 - area2)
    except ValueError:
        return "Invalid input: Please enter numeric values for areas."

if __name__ == '__main__':
    area1 = "45.67"
    area2 = "30.12"
    difference = calculate_area_difference(area1, area2)
    print(difference)