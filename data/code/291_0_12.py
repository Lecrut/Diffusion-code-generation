def compare_lengths(length1, length2):
    if length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    longer_length = compare_lengths(5.7, 3.4)
    print(longer_length)