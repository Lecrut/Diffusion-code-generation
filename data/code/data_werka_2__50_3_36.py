def calculate_area_difference(area1_str, area2_str):
    try:
        area1 = float(area1_str)
        area2 = float(area2_str)
        return abs(area1 - area2)
    except ValueError as e:
        print(f"Error converting to float: {e}")
        return None

if __name__ == '__main__':
    area1 = "45.67"
    area2 = "30.12"
    difference = calculate_area_difference(area1, area2)
    if difference is not None:
        print(difference)