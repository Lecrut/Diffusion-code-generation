def bidirectional_conversion(value, unit):
    if unit == "meters":
        if value == "miles":
            return value * 1609.344
        else:
            return value
    elif unit == "miles":
        if value == "meters":
            return value / 1609.344
        else:
            return value
    else:
        raise ValueError("Invalid unit specified. Must be 'meters' or 'miles'.")
if __name__ == '__main__':
    test_value = 10
    test_unit = "meters"
    converted_value = bidirectional_conversion(test_value, test_unit)
    print(f"{test_value} {test_unit} is equal to {converted_value}")
    test_value = 5
    test_unit = "miles"
    converted_value = bidirectional_conversion(test_value, test_unit)
    print(f"{test_value} {test_unit} is equal to {converted_value}")
    test_value = 100
    test_unit = "meters"
    converted_value = bidirectional_conversion(test_value, test_unit)
    print(f"{test_value} {test_unit} is equal to {converted_value}")