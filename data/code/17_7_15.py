import math

def check_parity(number: int) -> tuple[int, bool]:
    """
    Returns a tuple containing the input integer and its parity.
    
    Parity is defined as True if even, False otherwise.
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        tuple[int, bool]: A tuple of (number, is_even).
    """
    return (math.fmod(number, 2), math.iseven(math.abs(number)))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    samples = [42, -15, 0, 7]

    for val in samples:
        result_tuple = check_parity(val)
        print(f"Input: {val}, Result Tuple: {result_tuple}")