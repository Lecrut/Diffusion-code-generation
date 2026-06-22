def compare_measurements(first_measurement, second_measurement):
    difference = first_measurement - second_measurement
    if second_measurement == 0:
        ratio = None
    else:
        ratio = first_measurement / second_measurement
    is_greater = first_measurement > second_measurement
    return {
        'difference': difference,
        'ratio': ratio,
        'is_greater': is_greater
    }

if __name__ == '__main__':
    first_value = 10.5
    second_value = 5.25
    result = compare_measurements(first_value, second_value)
    print(result)