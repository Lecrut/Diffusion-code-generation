def compare_lengths(length1, length2):
    difference = abs(length1 - length2)
    
    if length1 > length2:
        description = "First length is greater"
    elif length2 > length1:
        description = "Second length is greater"
    else:
        description = "Both lengths are equal"
    
    return (difference, description)

if __name__ == '__main__':
    test_length_a = 7.5
    test_length_b = 4.8
    result = compare_lengths(test_length_a, test_length_b)
    print(result)