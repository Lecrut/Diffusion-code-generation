def parse_area(area_str):
    try:
        return float(area_str)
    except ValueError as e:
        print(f"Error: {e}")
        return None

def calculate_difference(area1_str, area2_str):
    area1 = parse_area(area1_str)
    area2 = parse_area(area2_str)
    
    if area1 is not None and area2 is not None:
        return abs(area1 - area2)
    return None

if __name__ == '__main__':
    area1 = "50.78"
    area2 = "35.45"
    difference = calculate_difference(area1, area2)
    if difference is not None:
        print(difference)