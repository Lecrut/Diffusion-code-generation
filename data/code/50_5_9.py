def calculate_area_differences(*areas):
    try:
        areas = [float(area) for area in areas]
        for i in range(len(areas) - 1):
            yield abs(areas[i] - areas[i + 1])
    except ValueError as e:
        print(f"Error: Invalid input string {e}")

if __name__ == '__main__':
    sample_areas = ["10.5", "4.2", "20", "5.5", "abc", "10"]
    for difference in calculate_area_differences(*sample_areas):
        print(difference)