def compare_lengths(len1, len2):
    if not isinstance(len1, (int, float)) or not isinstance(len2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    def determine_relationship(a, b):
        if a == b:
            return 'equal'
        elif a > b:
            return 'len1 is greater'
        else:
            return 'len2 is smaller'
    
    return determine_relationship(len1, len2)

if __name__ == '__main__':
    LENGTH1 = 40
    LENGTH2 = 20
    try:
        result = compare_lengths(LENGTH1, LENGTH2)
        print(result)
    except ValueError as e:
        print(e)