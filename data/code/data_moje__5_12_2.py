def get_larger_in_original_unit(meters_a, meters_b):
    centimeters_a = meters_a * 100
    centimeters_b = meters_b * 100
    if centimeters_a > centimeters_b:
        return meters_a
    else:
        return meters_b

if __name__ == '__main__':
    value_one = 1.5
    value_two = 2.3
    result = get_larger_in_original_unit(value_one, value_two)
    print(result)