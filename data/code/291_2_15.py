def compare_lengths(length1, unit1, length2, unit2):
    if unit1 == "inches":
        length1 *= 12
    elif unit1 != "feet":
        raise ValueError("Unsupported unit for length1")
    
    if unit2 == "inches":
        length2 *= 12
    elif unit2 != "feet":
        raise ValueError("Unsupported unit for length2")
    
    if length1 > length2:
        return f"{length1} inches"
    elif length1 < length2:
        return f"{length2} feet"

if __name__ == '__main__':
    result = compare_lengths(3, "feet", 48, "inches")
    print(result)