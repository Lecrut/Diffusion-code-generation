def calculate_length_difference(length1, length2):
    try:
        val1 = float(length1)
        val2 = float(length2)
    except (ValueError, TypeError):
        raise ValueError("Both inputs must be numeric values.")
    return val1 - val2

if __name__ == '__main__':
    result = calculate_length_difference(10.5, 3.2)
    print(result)
    
    result2 = calculate_length_difference(100, 50)
    print(result2)
    
    try:
        result3 = calculate_length_difference("10", "five")
        print(result3)
    except ValueError as e:
        print(e)