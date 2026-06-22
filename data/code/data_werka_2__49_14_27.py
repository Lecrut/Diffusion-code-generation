def compare_lengths(length1, length2):
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise ValueError("Both lengths must be numbers")
    
    lengths = {
        'length1': length1,
        'length2': length2
    }
    
    return max(lengths.values())

if __name__ == '__main__':
    sample_length1 = 18.4
    sample_length2 = 15.6
    try:
        longer_length = compare_lengths(sample_length1, sample_length2)
        print(longer_length)
    except ValueError as e:
        print(e)