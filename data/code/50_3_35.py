def convert_to_float(area_str):
    try:
        return float(area_str)
    except ValueError as e:
        print(f"Error: {e}")
        return None

def calculate_area_difference(area1_str, area2_str):
    area1 = convert_to_float(area1_str)
    area2 = convert_to_float(area2_str)
    
    if area1 is not None and area2 is not None:
        return abs(area1 - area2)
    return None

if __name__ == '__main__':
    sample_area1 = "78.90"
    sample_area2 = "54.32"
    difference = calculate_area_difference(sample_area1, sample_area2)
    
    if difference is not None:
        print(difference)