def compare_lengths(length1, length2):
    difference = abs(length1 - length2)
    if length1 > length2:
        result_string = "First length is greater"
    elif length2 > length1:
        result_string = "Second length is greater"
    else:
        result_string = "Both lengths are equal"
    return (difference, result_string)

if __name__ == '__main__':
    sample_length1 = 5.7
    sample_length2 = 3.2
    print(compare_lengths(sample_length1, sample_length2))