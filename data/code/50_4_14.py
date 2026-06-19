def calculate_area_difference(area1_str, area2_str):
    try:
        first_area = float(area1_str)
        second_area = float(area2_str)
        return abs(first_area - second_area)
    except ValueError as e:
        print(f"Error converting to float: {e}")
        return None

if __name__ == '__main__':
    sample_area_one = "75.2"
    sample_area_two = "20.8"
    result_difference = calculate_area_difference(sample_area_one, sample_area_two)
    if result_difference is not None:
        print(result_difference)