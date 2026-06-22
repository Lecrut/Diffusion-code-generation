def compare_lengths(length1, length2):
    return "length1 is larger" if length1 > length2 else "length2 is larger"

if __name__ == '__main__':
    LENGTH_ONE = 25
    LENGTH_TWO = 30
    result = compare_lengths(LENGTH_ONE, LENGTH_TWO)
    print(result)