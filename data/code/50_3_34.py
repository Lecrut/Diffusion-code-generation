def calculate_area_difference(area1_str, area2_str):
    try:
        area1 = float(area1_str)
        area2 = float(area2_str)
        return abs(area1 - area2)
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    area1 = "50.5"
    area2 = "30.2"
    difference = calculate_area_difference(area1, area2)
    if difference is not None:
        print(difference)