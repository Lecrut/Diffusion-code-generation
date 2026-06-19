def validate_length(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Length must be a number")

def compare_lengths(len1, len2):
    validate_length(len1)
    validate_length(len2)
    
    if len1 == len2:
        return 'equal'
    elif len1 > len2:
        return 'len1 is greater'
    else:
        return 'len2 is smaller'

if __name__ == '__main__':
    length1 = 35
    length2 = 40
    try:
        result = compare_lengths(length1, length2)
        print(result)
    except ValueError as e:
        print(e)