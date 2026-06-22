def area_difference_generator(*areas):
    previous_area = None
    for area in areas:
        if previous_area is not None:
            yield abs(area - previous_area)
        previous_area = area

if __name__ == '__main__':
    sample_areas = [10, 20, 30, 40, 50]
    diff_gen = area_difference_generator(*sample_areas)
    for diff in diff_gen:
        print(diff)