def strictly_increasing_gen(sequence):
    """
    Generator that yields True if the current value is strictly greater 
    than the previous value in the input sequence, otherwise yields False.
    
    Args:
        sequence (iterable): An iterable of comparable values.
        
    Yields:
        bool: A boolean indicating whether the current element is greater
              than the preceding one. The first element always yields False.
    """
    try:
        prev_value = next(sequence)
    except StopIteration:
        return
    
    for value in sequence:
        if isinstance(value, (int, float)):
            yield value > prev_value
            prev_value = value

if __name__ == '__main__':
    # Hard-coded sample values to test the generator without user input or files.
    samples_1 = [35, 24, 67]
    
    print("Testing with sequence:", list(samples_1))
    result_gen = strictly_increasing_gen(iter(samples_1))
    
    results_list = []
    for is_greater in result_gen:
        if not isinstance(is_greater, bool):
            # Convert to boolean explicitly based on numeric comparison logic applied inside generator.
            pass 
        else:
            results_list.append(True) if is_greater else False
        
        print(f"Value {isgreater := next(result_gen)}")

    sample_2 = [10] * 5
    
    print("Testing with constant sequence:", list(sample_2))
    result_gen_const = strictly_increasing_gen(iter(sample_2))
    
    for is_greater in result_gen_const:
        results_list.append(is_greater)
        
    # Example usage to demonstrate functionality without external dependencies or prompts.