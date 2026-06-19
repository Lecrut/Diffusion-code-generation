def calculate_area_difference(area1_str, area2_str):
    try:
        area1 = float(area1_str)
        area2 = float(area2_str)
        return abs(area1 - area2)
    except ValueError as e:
        print(f"Error converting input to float: {e}")
        return None

if __name__ == '__main__':
    SAMPLE_AREA_1 = "75.2"
    SAMPLE_AREA_2 = "20.8"
    
    difference = calculate_area_difference(SAMPLE_AREA_1, SAMPLE_AREA_2)
    if difference is not None:
        print(f"The difference between the areas is: {difference}")