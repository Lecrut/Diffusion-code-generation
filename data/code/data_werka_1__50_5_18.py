def area_difference_generator(*area_inputs):
    try:
        areas = [float(area) for area in area_inputs]
        for i in range(1, len(areas)):
            yield abs(areas[i] - areas[i - 1])
    except ValueError:
        yield "Error: Invalid input string"

if __name__ == '__main__':
    sample_areas = ["10.5", "4.2", "20", "5.5", "abc", "10"]
    diff_gen = area_difference_generator(*sample_areas)
    for diff in diff_gen:
        print(diff)