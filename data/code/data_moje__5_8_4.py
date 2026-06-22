def compare_lengths(length1, length2):
    diff = abs(length1 - length2)
    if length1 > length2:
        description = "The first length is greater"
    elif length2 > length1:
        description = "The second length is greater"
    else:
        description = "The lengths are equal"
    return diff, description

if __name__ == '__main__':
    val1 = 10.5
    val2 = 7.2
    result = compare_lengths(val1, val2)
    print(result)