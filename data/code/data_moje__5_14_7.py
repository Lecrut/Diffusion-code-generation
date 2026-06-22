def compare_lengths(value1, unit1, value2, unit2):
    conversion_factor = 2.54
    if unit1 == "inches":
        normalized1 = value1 * conversion_factor
    elif unit1 == "centimeters":
        normalized1 = value1
    else:
        raise ValueError(f"Unsupported unit: {unit1}")

    if unit2 == "inches":
        normalized2 = value2 * conversion_factor
    elif unit2 == "centimeters":
        normalized2 = value2
    else:
        raise ValueError(f"Unsupported unit: {unit2}")

    if normalized1 > normalized2:
        return f"{value1} {unit1} is greater than {value2} {unit2}"
    elif normalized1 < normalized2:
        return f"{value1} {unit1} is less than {value2} {unit2}"
    else:
        return f"{value1} {unit1} is equal to {value2} {unit2}"

if __name__ == "__main__":
    result = compare_lengths(10, "inches", 25, "centimeters")
    print(result)