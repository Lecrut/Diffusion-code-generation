def compare_lengths(length1, length2):
    return "length1 is larger" if length1 > length2 else "length2 is larger"

if __name__ == '__main__':
    length1 = 10
    length2 = 20
    result = compare_lengths(length1, length2)
    print(result)