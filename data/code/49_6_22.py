def compare_lengths(length1, length2):
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise ValueError("Both lengths must be numbers")
    
    return "length1 is larger" if length1 > length2 else "length2 is larger"

if __name__ == '__main__':
    try:
        length1 = 10
        length2 = 5
        result = compare_lengths(length1, length2)
        print(result)
    except ValueError as e:
        print(e)

    try:
        length1 = 'a'
        length2 = 5
        result = compare_lengths(length1, length2)
        print(result)
    except ValueError as e:
        print(e)