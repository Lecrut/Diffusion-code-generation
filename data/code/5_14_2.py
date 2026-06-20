def compare_lengths(length_inches, length_centimeters):
    inches_to_cm = 2.54
    length1_cm = length_inches * inches_to_cm
    length2_cm = length_centimeters

    if length1_cm > length2_cm:
        return f"{length_inches} inches ({length1_cm} cm) is greater than {length2_cm} cm"
    elif length1_cm < length2_cm:
        return f"{length2_cm} cm is greater than {length_inches} inches ({length1_cm} cm)"
    else:
        return f"{length_inches} inches ({length1_cm} cm) is equal to {length2_cm} cm"

if __name__ == '__main__':
    result = compare_lengths(10, 25.4)
    print(result)