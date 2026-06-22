def compare_lengths(length1: float, length2: float) -> tuple:
    abs_diff = abs(length1 - length2)
    if length1 > length2:
        description = "length1 is greater"
    elif length2 > length1:
        description = "length2 is greater"
    else:
        description = "lengths are equal"
    return (abs_diff, description)

if __name__ == '__main__':
    result = compare_lengths(10.5, 5.2)
    print(result)