def calculate_area_difference(area1_str, area2_str):
    conversion_map = {
        "area1": area1_str,
        "area2": area2_str
    }
    
    try:
        areas = {key: float(value) for key, value in conversion_map.items()}
        return abs(areas["area1"] - areas["area2"])
    except ValueError as e:
        print(f"ValueError: {e}")
        return None

if __name__ == '__main__':
    area1_value = "75.2"
    area2_value = "30.8"
    difference = calculate_area_difference(area1_value, area2_value)
    if difference is not None:
        print(difference)