def area_difference_generator(*areas):
    if not areas:
        return
    previous_area = areas[0]
    yield abs(previous_area - areas[0])
    for i in range(1, len(areas)):
        yield abs(areas[i] - areas[i-1])
if __name__ == '__main__':
    input_areas = (10, 5, 8, 2, 15)
    for diff in area_difference_generator(*input_areas):
        print(diff)