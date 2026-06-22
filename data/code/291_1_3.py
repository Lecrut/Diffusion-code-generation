def compare_lengths(length1: float, unit1: str, length2: float, unit2: str) -> str:
    if unit1 == 'cm' and unit2 == 'cm':
        return f"{min(length1, length2)} cm"
    elif unit1 == 'm' and unit2 == 'cm':
        length1_cm = length1 * 100
        return f"{min(length1_cm, length2)} cm" if length1_cm < length2 else f"{length2} {unit2}"
    elif unit1 == 'cm' and unit2 == 'm':
        length2_cm = length2 * 100
        return f"{min(length1, length2_cm)} cm" if length1 < length2_cm else f"{length2} {unit2}"
    else:
        raise ValueError("Unsupported units")

if __name__ == '__main__':
    print(compare_lengths(50, 'cm', 3, 'm'))
    print(compare_lengths(2.5, 'm', 250, 'cm'))