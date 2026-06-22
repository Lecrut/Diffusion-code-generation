def area_difference_generator(*areas):
    previous_area = None
    for area in areas:
        if previous_area is not None:
            yield abs(area - previous_area)
        previous_area = area

if __name__ == '__main__':
    sample_areas = [10, 25, 15, 30, 40]
    differences = area_difference_generator(*sample_areas)
    for diff in differences:
        print(diff)