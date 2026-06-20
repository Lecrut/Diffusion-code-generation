def compare_lengths(length_in, length_cm):
    length_in_cm = length_in * 2.54
    if length_in_cm > length_cm:
        return "Inches is longer"
    elif length_in_cm < length_cm:
        return "Centimeters is longer"
    else:
        return "Lengths are equal"

if __name__ == '__main__':
    result = compare_lengths(10, 25)
    print(result)