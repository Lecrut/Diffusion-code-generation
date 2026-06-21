def compare_lengths(length1, length2):
    if not isinstance(length1, (int, float)) or not isinstance(length2, (int, float)):
        raise ValueError("Both lengths must be numbers")
    
    return max(length1, length2)

if __name__ == '__main__':
    sample_lengths = {
        "length1": 18.4,
        "length2": 22.9
    }
    
    try:
        longer_length = compare_lengths(sample_lengths["length1"], sample_lengths["length2"])
        print(longer_length)
    except ValueError as e:
        print(e)