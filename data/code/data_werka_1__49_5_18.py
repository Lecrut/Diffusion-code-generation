def compare_lengths(len1, len2):
    if not isinstance(len1, (int, float)) or not isinstance(len2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    if len1 == len2:
        return 'equal'
    elif len1 > len2:
        return 'len1 is greater'
    else:
        return 'len2 is smaller'

if __name__ == '__main__':
    LENGTH_THRESHOLD = 0.0001
    length1 = 50.0
    length2 = 49.9999

    result = compare_lengths(length1, length2)
    print(result)