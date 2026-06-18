def strictly_increasing_generator(sequence):
    """
    Generator that yields True if the current value is strictly greater 
    than the previous value in the input sequence, otherwise yields False.
    
    Args:
        sequence (iterable): An iterable of comparable values.
        
    Yields:
        bool: True if current > previous, else False. The first element always 
              yields False as there is no predecessor to compare against.
    """
    try:
        prev_value = next(sequence)
    except StopIteration:
        return
    
    for current_value in sequence:
        yield (current_value > prev_value)
        prev_value = current_value

if __name__ == '__main__':
    # Hard-coded sample values to test the generator without user input
    sample_data = [10, 5, 20, 30, 40, 80]
    
    print("Input sequence:", sample_data)
    print("\nComparison results:")
    
    result_generator = strictly_increasing_generator(sample_data)
    
    for is_greater in result_generator:
        # We need to track the index or value context manually since 
        # we consumed the generator. Let's re-run logic inline for clarity in output.
        pass
    
    # Re-implementing slightly inside main loop for direct printing with values
    iterator = iter(sample_data)
    try:
        prev_val = next(iterator)
    except StopIteration:
        print("Sequence is empty.")
    
    else:
        print(f"First value ({prev_val}): No previous comparison -> False")
        
        for curr_val in iterator:
            result = (curr_val > prev_val)
            status_str = "True" if result else "False"
            relation_desc = f"{prev_val} < {curr_val}" if result else f"{prev_val} >= {curr_val}"
            print(f"Current value ({curr_val}): {status_str} ({relation_desc})")
            
            prev_val = curr_val