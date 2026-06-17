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
    print(bidirectional_conversion("10", "meters"))
    print(bidirectional_conversion("5", "miles"))
    print(bidirectional_conversion("10", "meters"))
    print(bidirectional_conversion("5", "miles"))