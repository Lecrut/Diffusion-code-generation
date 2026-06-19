def compare_lengths(length1, length2):
    abs_difference = abs(length1 - length2)
    if length1 > length2:
        description = "length1 is greater"
    elif length2 > length1:
        description = "length2 is greater"
    else:
        description = "both lengths are equal"
    return (abs_difference, description)

if __name__ == '__main__':
    sample_length1 = 5.75
    sample_length2 = 3.25
    result = compare_lengths(sample_length1, sample_length2)
    print(result)