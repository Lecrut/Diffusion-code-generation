def compare_lengths(length1, length2):
    return "length1" if length1 > length2 else "length2"

if __name__ == '__main__':
    length1 = 15
    length2 = 10
    result = compare_lengths(length1, length2)
    print(result)