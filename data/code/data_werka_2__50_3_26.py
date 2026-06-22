def parse_area(area_str):
    try:
        return float(area_str)
    except ValueError as e:
        print(f"Error: {e}")
        return None

def calculate_difference(area1, area2):
    if area1 is not None and area2 is not None:
        return abs(area1 - area2)
    return None

if __name__ == '__main__':
    area_samples = {
        "area1": "78.9",
        "area2": "54.3"
    }
    
    parsed_areas = {key: parse_area(value) for key, value in area_samples.items()}
    
    difference = calculate_difference(parsed_areas["area1"], parsed_areas["area2"])
    
    if difference is not None:
        print(difference)