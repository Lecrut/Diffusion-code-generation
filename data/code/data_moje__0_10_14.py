def convert_length(length, target_unit):
    if target_unit == "meters":
        return length
    elif target_unit == "feet":
        return length * 3.28084
    elif target_unit == "kilometers":
        return length / 1000.0
    else:
        raise ValueError(f"Unsupported unit: {target_unit}")

if __name__ == '__main__':
    print(convert_length(100, "feet"))
    print(convert_length(1, "kilometers"))
    print(convert_length(50, "meters"))