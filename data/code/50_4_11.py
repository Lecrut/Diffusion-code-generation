def calculate_area_difference(area1_str, area2_str):
    try:
        area1 = float(area1_str)
        area2 = float(area2_str)
    except ValueError as e:
        return f"ValueError: {e}"
    
    return abs(area1 - area2)

if __name__ == '__main__':
    sample_area1 = "75.2"
    sample_area2 = "30.8"
    difference = calculate_area_difference(sample_area1, sample_area2)
    print(difference)