def validate_area(area_str):
    try:
        return float(area_str)
    except ValueError:
        raise ValueError(f"Invalid area input: {area_str}")

def absolute_difference_generator(*areas):
    areas = list(map(validate_area, areas))
    for i in range(1, len(areas)):
        yield abs(areas[i] - areas[i-1])

if __name__ == '__main__':
    areas = ["10.5", "4.2", "20", "5.5", "abc"]
    try:
        diff_gen = absolute_difference_generator(*areas)
        for diff in diff_gen:
            print(diff)
    except ValueError as e:
        print(e)