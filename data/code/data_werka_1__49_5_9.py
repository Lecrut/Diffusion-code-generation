def validate_lengths(len1, len2):
    if not isinstance(len1, (int, float)) or not isinstance(len2, (int, float)):
        raise ValueError("Both inputs must be numbers")

def compare_lengths(len1, len2):
    validate_lengths(len1, len2)
    if len1 == len2:
        return 'equal'
    elif len1 > len2:
        return 'len1 is greater'
    else:
        return 'len2 is smaller'

if __name__ == '__main__':
    length1 = 35
    length2 = 20
    try:
        result = compare_lengths(length1, length2)
        print(result)
    except ValueError as e:
        print(e)