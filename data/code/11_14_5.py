def calculate_ratios(length_pairs):
    """
    Takes a list of length pairs (tuples) and returns a new list containing 
    the ratio for every pair, filtering out any pairs where the denominator is zero.
    
    Args:
        length_pairs (list[tuple]): A list of tuples where each tuple contains two integers.
                                   Each tuple represents (length1, length2).
        
    Returns:
        list[float]: A list of floats representing the ratio (length1 / length2) 
                    for valid pairs only. If denominator is zero or pair is invalid, it's skipped.
    
    Raises:
        ValueError: If an element in the input list is not a tuple with exactly two numeric elements.
    """
    result_ratios = []
    
    for item in length_pairs:
        if isinstance(item, (list, tuple)):
            len1, len2 = item[0], item[1]
            
            # Ensure both values are numbers and denominator is not zero
            try:
                float(len1)
                float(len2)
                
                if len2 == 0:
                    continue
                    
                result_ratios.append(float(len1 / len2))
            except (TypeError, ValueError):
                raise ValueError("Invalid pair format or non-numeric values in the list.")
        else:
            raise ValueError(f"Unexpected item type {type(item)} in input list. Expected tuple/list of two numbers.")

    return result_ratios

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction)
    sample_data = [
        (10, 5),       # Ratio: 2.0
        (7, 49),       # Ratio: 0.1428...
        (3, 0),        # Skipped due to zero denominator
        (6, -3),       # Valid negative ratio (-2.0)
    ]

    calculated_results = calculate_ratios(sample_data)

    print("Calculated ratios:", calculated_results)