def calculate_area_difference(area1_str, area2_str):
    try:
        area1 = float(area1_str)
        area2 = float(area2_str)
        return abs(area1 - area2)
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    areas = {
        "Area One": "45.67",
        "Area Two": "30.12"
    }
    difference = calculate_area_difference(areas["Area One"], areas["Area Two"])
    if difference is not None:
        print(difference)