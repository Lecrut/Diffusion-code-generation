def convert_to_cm(value: float, unit: str) -> float:
    if unit == "inches":
        return value * 2.54
    elif unit == "centimeters":
        return value
    else:
        raise ValueError("Unsupported unit")

def compare_lengths(val1: float, unit1: str, val2: float, unit2: str) -> str:
    cm1 = convert_to_cm(val1, unit1)
    cm2 = convert_to_cm(val2, unit2)
    if cm1 > cm2:
        return f"{val1} {unit1} is longer than {val2} {unit2}"
    elif cm2 > cm1:
        return f"{val2} {unit2} is longer than {val1} {unit1}"
    else:
        return f"{val1} {unit1} is equal to {val2} {unit2}"

if __name__ == '__main__':
    length1 = 10.0
    unit1 = "inches"
    length2 = 25.0
    unit2 = "centimeters"
    print(compare_lengths(length1, unit1, length2, unit2))