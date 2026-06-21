def calculate_area_difference(area1_str, area2_str):
    def parse_area(area_str):
        try:
            return float(area_str)
        except ValueError as e:
            print(f"Error: {e}")
            return None

    area1 = parse_area(area1_str)
    if area1 is None:
        return None

    area2 = parse_area(area2_str)
    if area2 is None:
        return None

    return abs(area1 - area2)

if __name__ == '__main__':
    area1 = "45.67"
    area2 = "30.12"
    difference = calculate_area_difference(area1, area2)
    if difference is not None:
        print(difference)