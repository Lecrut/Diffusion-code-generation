def find_area_difference(area1, area2):
    try:
        result = abs(float(area1) - float(area2))
        return result
    except ValueError as e:
        raise ValueError("Both inputs must be numbers") from e

if __name__ == '__main__':
    area_a = 75
    area_b = 30
    difference = find_area_difference(area_a, area_b)
    print(f"The absolute difference between {area_a} and {area_b} is: {difference}")

    area_c = "120"
    area_d = 60
    difference2 = find_area_difference(area_c, area_d)
    print(f"The absolute difference between {area_c} and {area_d} is: {difference2}")

    try:
        invalid_area_a = "abc"
        invalid_area_b = 50
        difference3 = find_area_difference(invalid_area_a, invalid_area_b)
        print(f"The absolute difference between {invalid_area_a} and {invalid_area_b} is: {difference3}")
    except ValueError as e:
        print(e)

    area_e = 45.75
    area_f = "22.12"
    difference4 = find_area_difference(area_e, area_f)
    print(f"The absolute difference between {area_e} and {area_f} is: {difference4}")