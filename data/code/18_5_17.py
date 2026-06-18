def strictly_increasing_generator(sequence):
    """
    Generator that yields True if the current value is strictly greater 
    than the previous value in the input sequence, otherwise yields False.
    
    Args:
        sequence (iterable): An iterable of comparable values.
        
    Yields:
        bool: True if current > previous, else False. The first element 
              always yields False as there is no previous value to compare with.
    """
    try:
        prev = next(sequence)
    except StopIteration:
        return
    
    for curr in sequence:
        yield (curr > prev)
        prev = curr

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    # No user input, command-line arguments, or network access used.
    
    # Sample 1: Increasing then decreasing
    data1 = [3, 5, 2, 8, 4]
    result1 = list(strictly_increasing_generator(data1))
    print(f"Input: {data1}")
    print(f"Output (bools): {result1}")
    
    # Sample 2: All decreasing
    data2 = [5, 3, 1, -2]
    result2 = list(strictly_increasing_generator(data2))
    print(f"\nInput: {data2}")
    print(f"Output (bools): {result2}")
    
    # Sample 3: All increasing
    data3 = [0, 1, 5, 8]
    result3 = list(strictly_increasing_generator(data3))
    print(f"\nInput: {data3}")
    print(f"Output (bools): {result3}")
    
    # Sample 4: Single element
    data4 = [10]
    result4 = list(strictly_increasing_generator(data4))
    print(f"\nInput: {data4}")
    print(f"Output (bools): {result4}")