def area_difference_generator(*areas):
    previous_area = None
    for current_area in areas:
        if previous_area is not None:
            difference = abs(current_area - previous_area)
            yield difference
        previous_area = current_area

if __name__ == '__main__':
    sample_areas = [7, 14, 28, 56]
    differences = area_difference_generator(*sample_areas)
    for diff in differences:
        print(diff)