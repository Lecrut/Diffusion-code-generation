def convert_length(length, unit):
    if unit == 'm':
        return length
    elif unit == 'ft':
        return length * 3.28084
    else:
        raise ValueError("Invalid unit type. Must be 'm' or 'ft'.")
if __name__ == '__main__':
    length_m = 10
    unit_m = 'm'
    result_m = convert_length(length_m, unit_m)
    print(f"Length: {length_m} {unit_m} -> {result_m} {unit_m}")
    length_ft = 10
    unit_ft = 'ft'
    result_ft = convert_length(length_ft, unit_ft)
    print(f"Length: {length_ft} {unit_ft} -> {result_ft} {unit_ft}")