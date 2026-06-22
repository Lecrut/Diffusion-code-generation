def parse_area(area_str):
    try:
        return float(area_str)
    except ValueError as e:
        print(f"Error: {e}")
        return None

def validate_areas(area1, area2):
    if area1 is None or area2 is None:
        print("Error: One or both areas are invalid.")
        return False
    return True

def calculate_area_difference(area1_str, area2_str):
    area1 = parse_area(area1_str)
    area2 = parse_area(area2_str)
    
    if validate_areas(area1, area2):
        return abs(area1 - area2)
    return None

if __name__ == '__main__':
    area1 = "45.67"
    area2 = "30.12"
    difference = calculate_area_difference(area1, area2)
    if difference is not None:
        print(difference)