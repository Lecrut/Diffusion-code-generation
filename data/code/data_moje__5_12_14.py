def compare_lengths_in_cm(length1, length2):
    length1_cm = length1 * 100
    length2_cm = length2 * 100
    if length1_cm >= length2_cm:
        return length1
    else:
        return length2

if __name__ == '__main__':
    print(compare_lengths_in_cm(1.5, 2.3))
    print(compare_lengths_in_cm(5, 4.9))
    print(compare_lengths_in_cm(0.1, 0.1))