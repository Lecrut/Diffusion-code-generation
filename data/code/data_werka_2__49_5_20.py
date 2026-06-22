def compare_lengths(len1, len2):
    if not isinstance(len1, (int, float)) or not isinstance(len2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    COMPARISON_EQUAL = 'equal'
    COMPARISON_LEN1_GREATER = 'len1 is greater'
    COMPARISON_LEN2_SMALLER = 'len2 is smaller'
    
    if len1 == len2:
        return COMPARISON_EQUAL
    elif len1 > len2:
        return COMPARISON_LEN1_GREATER
    else:
        return COMPARISON_LEN2_SMALLER

if __name__ == '__main__':
    length1 = 75
    length2 = 75
    try:
        result = compare_lengths(length1, length2)
        print(result)
    except ValueError as e:
        print(e)

    length1 = 60
    length2 = 90
    try:
        result = compare_lengths(length1, length2)
        print(result)
    except ValueError as e:
        print(e)

    length1 = 120
    length2 = 60
    try:
        result = compare_lengths(length1, length2)
        print(result)
    except ValueError as e:
        print(e)