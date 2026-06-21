def compare_values(value1, value2):
    if value1 > value2:
        return "First value is greater than the second value."
    elif value1 < value2:
        return "First value is less than the second value."
    else:
        return "First value is equal to the second value."

if __name__ == '__main__':
    SAMPLE_VALUE_1 = 30
    SAMPLE_VALUE_2 = 60
    result = compare_values(SAMPLE_VALUE_1, SAMPLE_VALUE_2)
    print(result)