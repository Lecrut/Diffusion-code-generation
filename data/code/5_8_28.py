def compare_lengths(length1, length2):
    difference = abs(length1 - length2)
    if length1 > length2:
        description = "length1 is greater"
    elif length2 > length1:
        description = "length2 is greater"
    else:
        description = "both lengths are equal"
    return (difference, description)

if __name__ == '__main__':
    result = compare_lengths(5.75, 3.25)
    print(result)