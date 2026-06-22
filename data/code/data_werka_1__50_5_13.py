def area_difference_generator(*area_strs):
    try:
        areas = [float(area) for area in area_strs]
        previous_area = None
        for area in areas:
            if previous_area is not None:
                yield abs(previous_area - area)
            previous_area = area
    except ValueError:
        print("Error: Invalid input string")

if __name__ == '__main__':
    area_values = ["10.5", "4.2", "20", "5.5", "abc", "10"]
    for difference in area_difference_generator(*area_values):
        print(difference)