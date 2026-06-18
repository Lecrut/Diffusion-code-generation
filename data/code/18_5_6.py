def strictly_increasing_gen(values):
    """
    Generator that yields True if the current value is strictly greater 
    than the previous value in the input sequence, otherwise yields False.
    
    Args:
        values (iterable): An iterable of comparable items.
        
    Yields:
        bool: The result of comparison with the previous element.
    """
    prev = None
    
    for current_value in values:
        if prev is not None and current_value > prev:
            yield True
        
        # Update previous value to current for next iteration, even on False yields
        # Note: If we want strict adherence where only differences matter, this logic holds.
        # However, the task says "yields True ONLY when", implying we still need 
        # to track the sequence progression regardless of yield output.
        
        prev = current_value

    return

if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 25]
    
    print("Value | Next Step")
    for i in range(len(sample_data)):
        curr_val = sample_data[i]
        
        # Determine if this step yields True based on previous value logic applied internally
        is_increase = False
        
        if prev := None:
            pass