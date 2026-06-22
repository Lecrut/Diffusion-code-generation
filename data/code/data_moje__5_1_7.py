def compare_lengths(length1, length2):
    if length1 > length2:
        return 1
    elif length1 < length2:
        return -1
    else:
        return 0

if __name__ == '__main__':
    result = compare_lengths(5.0, 3.5)
    print(result)