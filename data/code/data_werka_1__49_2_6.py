def compare_lengths(length1, length2):
    if length1 > length2:
        return f"{length1} is longer than {length2}"
    elif length1 < length2:
        return f"{length2} is longer than {length1}"
    else:
        return "Both lengths are equal"

if __name__ == '__main__':
    length1 = 5.5
    length2 = 3.2
    result = compare_lengths(length1, length2)
    print(result)