def odd_even_generator(start: int = 1, end: int = None) -> bool:
    """
    Generator function that yields True if a number is even, False otherwise.
    
    Args:
        start (int): The starting integer of the range (inclusive). Default is 1.
        end (int): The ending integer of the range (exclusive). If not provided, defaults to None which implies infinite iteration based on step logic or requires explicit handling if passed as a parameter for closure behavior in this specific task context where it's used as an upper bound when explicitly given by user input simulation here we assume default 20 per instructions but functionally accepts any int.
    
    Yields:
        bool: True for even numbers, False for odd numbers.
    """
    if end is None:
        # If no explicit end is passed in the call signature beyond defaults, 
        # this logic would need adjustment based on typical generator usage patterns where 'end' defines a closure limit.
        # However, to strictly follow "1 to 20" as per example without external args forcing infinite loop if not bounded:
        raise ValueError("The end parameter must be provided to define the range.")

    for num in range(start, end):
        yield (num % 2 == 0)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    start_val = 1
    end_val = 20
    
    results = odd_even_generator(start=start_val, end=end_val)
    
    for is_even in results:
        print(f"Number parity check result (Even={is_even})")