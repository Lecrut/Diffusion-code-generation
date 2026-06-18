def strictly_increasing_generator(sequence):
    """
    Generator function that yields True if the current value is strictly greater 
    than the previous value in the input sequence, otherwise yields False.
    
    Args:
        sequence (iterable): An iterable of comparable values.
        
    Yields:
        bool: True if current > previous, else False. The first element always yields False.
    """
    try:
        prev = next(sequence)
    except StopIteration:
        return
    
    for curr in sequence:
        yield (curr > prev)
        prev = curr

if __name__ == '__main__':
    # Hard-coded sample values to test the generator without user input or files.
    sample_data = [1, 3, 2, 4, 5]
    
    result_gen = strictly_increasing_generator(sample_data)
    
    print("Input:", sample_data)
    print("Output (True/False):")
    for is_greater in result_gen:
        print(is_greater)