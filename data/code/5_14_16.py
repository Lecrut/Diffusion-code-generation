import math

def compare_lengths(length1, unit1, length2, unit2):
    inches_per_inch = 1.0
    inches_per_cm = 0.393700787
    
    if unit1 == "inches" and unit2 == "centimeters":
        length1_in = length1 * inches_per_inch
        length2_in = length2 * inches_per_cm
    elif unit1 == "centimeters" and unit2 == "inches":
        length1_in = length1 * inches_per_cm
        length2_in = length2 * inches_per_inch
    else:
        raise ValueError("Supported units are 'inches' and 'centimeters'")
    
    if math.isclose(length1_in, length2_in, rel_tol=1e-9):
        return "equal"
    elif length1_in > length2_in:
        return "greater"
    else:
        return "less"

if __name__ == '__main__':
    result = compare_lengths(10, "inches", 25.4, "centimeters")
    print(result)