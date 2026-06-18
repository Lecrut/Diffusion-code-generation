def get_number_and_parity(number: int) -> tuple[int, bool]:
    """
    Takes an integer and returns a tuple containing the input number 
    and its parity (True if even, False if odd).
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        tuple[int, bool]: A tuple of (number, is_even).
    """
    return number, not isinstance(number % 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    samples = [0, 1, -5, 42]
    
    print("Input | Parity (Even=True)")
    for num in samples:
        result_num, is_even = get_number_and_parity(num)
        parity_str = "True" if is_even else "False"
        print(f"{num}          | {parity_str}")