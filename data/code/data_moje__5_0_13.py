def calculate_length_difference(length1, length2):
    try:
        val1 = float(length1)
    except (TypeError, ValueError):
        raise TypeError(f"Invalid input for length1: {length1}. Expected a numeric value.")
    try:
        val2 = float(length2)
    except (TypeError, ValueError):
        raise TypeError(f"Invalid input for length2: {length2}. Expected a numeric value.")
    
    difference = val1 - val2
    return abs(difference)

if __name__ == '__main__':
    l1 = 15.5
    l2 = 10.2
    result = calculate_length_difference(l1, l2)
    print(result)