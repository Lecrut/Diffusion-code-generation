def compare_lengths(length1, length2):
    if not (isinstance(length1, (int, float)) and isinstance(length2, (int, float))):
        raise ValueError("Both lengths must be numbers.")
    
    return (min(length1, length2), max(length1, length2))

if __name__ == '__main__':
    sample_length1 = 50
    sample_length2 = 30
    try:
        result = compare_lengths(sample_length1, sample_length2)
        print(result)
    except ValueError as e:
        print(e)