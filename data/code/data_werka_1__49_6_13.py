def compare_lengths(length1, length2):
    return "Length 1 is larger" if length1 > length2 else ("Length 2 is larger" if length2 > length1 else "Both lengths are equal")

if __name__ == '__main__':
    length1 = 10
    length2 = 20
    result = compare_lengths(length1, length2)
    print(result)