def convert_length(length, unit):
    if unit == 'm':
        return length * 3.28084
    elif unit == 'ft':
        return length / 3.28084
    else:
        raise ValueError("Unsupported unit type")

if __name__ == '__main__':
    result_m = convert_length(1, 'm')
    print(result_m)
    result_ft = convert_length(1, 'ft')
    print(result_ft)