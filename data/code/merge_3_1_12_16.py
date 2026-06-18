def filter_valid_weights(weight_list):
    """
    Takes a list of weight measurements (strings) and returns a new list 
    containing only valid, positive numerical weights.
    
    Args:
        weight_list (list[str]): List of strings representing potential weights.
        
    Returns:
        list[float]: A filtered list of floats that are numerically valid and positive.
                     Invalid entries or non-positive numbers result in a ValueError 
                     being raised if they were expected to be processed, but since the 
                     task asks for graceful handling without crashing on bad input data 
                     (implied by 'handling potential exceptions gracefully'), we catch errors 
                     per item rather than failing the whole list. However, strictly following 
                     standard exception behavior where an invalid conversion should raise:
                     
    Note: The prompt says "handle... gracefully". In Python functional contexts without explicit 
    error handling instructions for individual items, a ValueError is typically raised on bad input.
    To be truly graceful while returning valid data, we will catch the ValueError during iteration 
    and skip invalid entries instead of propagating them, ensuring no crash occurs even with dirty data.
    
    Raises:
        None (handled internally) or potentially if all items are invalid? No, returns empty list then.
        
    Example:
        >>> filter_valid_weights(["10", "20.5", "-5", "abc"])
        [10.0, 20.5]
    """
    valid_weights = []
    
    for item in weight_list:
        try:
            # Attempt to convert the string to a float
            num_value = float(item)
            
            # Check if the number is positive (greater than zero)
            if num_value > 0:
                valid_weights.append(num_value)
        except ValueError:
            # Gracefully handle non-numeric strings by skipping them
            continue
            
    return valid_weights

if __name__ == '__main__':
    # Hard-coded sample values including invalid entries, negatives, and floats
    sample_data = ["10.5", "20", "-3.7", "abc", "", "  ", "0", "42"]
    
    result = filter_valid_weights(sample_data)
    
    print("Filtered valid positive weights:", result)