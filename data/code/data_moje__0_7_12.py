def convert_length(value, unit_type):
    if unit_type == 'm':
        return value * 3.28084
    elif unit_type == 'ft':
        return value / 3.28084
    else:
        raise ValueError("Invalid unit type. Use 'm' or 'ft'.")

if __name__ == '__main__':
    print(convert_length(10, 'm'))
    print(convert_length(10, 'ft'))