def compare_lengths(meter1, meter2):
    if meter1 > meter2:
        return meter1
    elif meter2 > meter1:
        return meter2
    else:
        return None

if __name__ == '__main__':
    length_a = 5.0
    length_b = 7.5
    longer_length = compare_lengths(length_a, length_b)
    if longer_length is not None:
        print(f"The longer length is {longer_length} meters.")
    else:
        print("Both lengths are equal.")

    length_c = 10.0
    length_d = 10.0
    longer_length2 = compare_lengths(length_c, length_d)
    if longer_length2 is not None:
        print(f"The longer length is {longer_length2} meters.")
    else:
        print("Both lengths are equal.")