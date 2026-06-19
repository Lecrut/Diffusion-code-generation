def compare_lengths(length1, length2):
    return "Length 1 is larger" if length1 > length2 else "Length 2 is larger"

if __name__ == '__main__':
    length1 = 10
    length2 = 20
    print(compare_lengths(length1, length2))