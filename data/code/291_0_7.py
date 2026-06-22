def compare_lengths(meter1, meter2):
    if not (isinstance(meter1, (int, float)) and isinstance(meter2, (int, float))):
        raise ValueError("Both inputs must be numbers (int or float).")
    if meter1 > meter2:
        return meter1
    elif meter2 > meter1:
        return meter2
    else:
        return None

if __name__ == '__main__':
    length_a = 5.0
    length_b = 3.5
    longer_length = compare_lengths(length_a, length_b)
    print(f"The longer length is: {longer_length} meters")

    length_c = 2.5
    length_d = 2.5
    result = compare_lengths(length_c, length_d)
    if result is None:
        print("Both lengths are equal.")
    else:
        print(f"The longer length is: {result} meters")