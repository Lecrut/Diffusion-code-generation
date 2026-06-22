def compare_lengths(length1, length2):
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise ValueError("Both lengths must be numbers (int or float).")
    
    result = {
        'length1': length1,
        'length2': length2,
        'is_length1_greater': length1 > length2
    }
    return result

if __name__ == '__main__':
    try:
        sample_length1 = 25.5
        sample_length2 = 30.2
        result = compare_lengths(sample_length1, sample_length2)
        print(result)
    except ValueError as e:
        print(e)