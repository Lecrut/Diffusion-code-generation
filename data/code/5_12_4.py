def compare_lengths_in_cm(length1_m, length2_m):
    cm1 = length1_m * 100
    cm2 = length2_m * 100
    if cm1 >= cm2:
        return length1_m
    else:
        return length2_m

if __name__ == '__main__':
    result = compare_lengths_in_cm(1.5, 2.0)
    print(result)