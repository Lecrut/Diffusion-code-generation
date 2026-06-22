def compare_values(value1, value2):
    if value1 > value2:
        return "First value is greater than the second value."
    elif value1 < value2:
        return "First value is less than the second value."
    else:
        return "First value is equal to the second value."

if __name__ == '__main__':
    sample_value1 = 42
    sample_value2 = 27
    result = compare_values(sample_value1, sample_value2)
    print(result)