def compare_lengths(length1, length2):
    abs_difference = abs(length1 - length2)
    if length1 > length2:
        description = "The first length is greater."
    elif length2 > length1:
        description = "The second length is greater."
    else:
        description = "Both lengths are equal."
    
    return (abs_difference, description)

if __name__ == '__main__':
    sample_length1 = 5.75
    sample_length2 = 3.25
    result = compare_lengths(sample_length1, sample_length2)
    print(result)