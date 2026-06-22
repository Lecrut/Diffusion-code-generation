def compare_lengths(meter1, meter2):
    if meter1 > meter2:
        return meter1
    elif meter2 > meter1:
        return meter2
    else:
        return None
if __name__ == '__main__':
    length_a = 5.7
    length_b = 3.8
    result = compare_lengths(length_a, length_b)
    print(result)
    length_c = 4.2
    length_d = 4.2
    result2 = compare_lengths(length_c, length_d)
    print(result2)