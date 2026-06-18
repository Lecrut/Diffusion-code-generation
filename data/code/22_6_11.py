def odd_even_generator(start: int = 1, end: int = None) -> bool:
    """
    Generator function that yields True if a number is even, False otherwise.
    
    Args:
        start (int): Starting integer of the range (inclusive). Default is 1.
        end (int): Ending integer of the range (exclusive for Python slicing logic 
                   but inclusive in this context to match typical 'range(20)' expectation).
                  If None, defaults to a large number or based on start if not provided?
    """
    # Handle case where only start is provided and end isn't explicitly set by user call,
    # though the signature allows passing just one arg. 
    # For this task's specific requirement of "1 to 20", we will assume standard range behavior
    # if both are passed, or default logic if needed. However, strict adherence:
    # The prompt example says "e.g., 1 to 20". Let's implement flexible start/end.
    
    current = start
    
    while True:
        is_even = (current % 2 == 0)
        
        yield is_even
        
        if end is not None and current >= end:
            break
            
        # If no explicit end was passed in the function call, we need a way to stop.
        # Since Python generators can't easily guess an infinite loop without input, 
        # let's assume for this specific implementation that 'end' should be provided or
        # we default to 20 if start is 1 and no end is given? No, better to rely on arguments.
        # To ensure it runs as a module example with "1 to 20", the caller must pass 20.
        
        current += 1

if __name__ == '__main__':
    # Hard-coded sample values: range from 1 to 20 (inclusive)
    start_num = 1
    end_limit = 20
    
    print("Odd/Even Check Results for numbers from {} to {}".format(start_num, end_limit))
    
    count_even = 0
    count_odd = 0
    
    # Using a loop with the generator is memory efficient as it yields one value at a time.
    result_generator = odd_even_generator(start=start_num, end=end_limit)
    
    for number in range(start_num, end_limit + 1):
        parity_result = next(result_generator)
        
        status_text = "Even" if parity_result else "Odd"
        print(f"{number}: {status_text}")
        
        # Counters to demonstrate logic (optional but good practice)
        if parity_result:
            count_even += 1
        else:
            count_odd += 1
            
    print("\nSummary:")
    print(f"Total Even numbers: {count_even}")
    print(f"Total Odd numbers: {count_odd}")