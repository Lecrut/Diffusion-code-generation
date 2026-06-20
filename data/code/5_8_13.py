def compare_lengths(length1, length2):
    absolute_difference = abs(length1 - length2)
    if length1 > length2:
        description = "first length is greater"
    elif length2 > length1:
        description = "second length is greater"
    else:
        description = "lengths are equal"
    return (absolute_difference, description)

if __name__ == '__main__':
    result = compare_lengths(10.5, 8.2)
    print(result)