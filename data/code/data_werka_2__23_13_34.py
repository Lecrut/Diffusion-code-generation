def compare_values(value1, value2):
    if value1 > value2:
        return "First value is greater than the second value."
    elif value1 < value2:
        return "First value is less than the second value."
    else:
        return "First value is equal to the second value."

if __name__ == '__main__':
    first_value = 75
    second_value = 90
    comparison_result = compare_values(first_value, second_value)
    print(comparison_result)