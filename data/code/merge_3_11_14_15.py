def calculate_ratios(length_pairs):
    """
    Takes a list of tuples representing length pairs (length1, length2) 
    and returns a new list containing the calculated ratio (length1 / length2).
    
    Pairs where length2 is zero are filtered out.
    
    Args:
        length_pairs (list[tuple]): A list of tuples, each being (length1, length2).
        
    Returns:
        list[float]: A list of ratios calculated as length1 divided by length2 for valid pairs.
    """
    result = []
    for pair in length_pairs:
        if len(pair) != 2:
            continue
        _, denominator = pair
        if denominator == 0:
            continue
        numerator, _ = pair[0]
        ratio = numerator / denominator
        result.append(ratio)
    
    return result

if __name__ == '__main__':
    sample_data = [
        (10, 2),
        (5, 0),      # Will be filtered out due to zero denominator
        (8, 4),
        (-3, 6),
        (7, 7),
        (0, 9)       # Valid since numerator is not required for calculation logic here
    ]
    
    output = calculate_ratios(sample_data)
    print(output)