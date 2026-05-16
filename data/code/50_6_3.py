def area_difference_generator(*areas):
    if not areas:
        return
    previous_area = areas[0]
    yield abs(previous_area - areas[1])
    for i in range(1, len(areas) - 1):
        yield abs(areas[i] - areas[i+1])
if __name__ == '__main__':
    input_areas = (10, 20, 5, 15, 30)
    for diff in area_difference_generator(*input_areas):
        print(diff)