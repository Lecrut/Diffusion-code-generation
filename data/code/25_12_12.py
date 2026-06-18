import sys

def process_integers(integer_list):
    """
    Process a list of integers to determine if each is zero.
    
    Args:
        integer_list (list[int]): List of integers from input.
        
    Returns:
        list[bool]: A list indicating whether each element in the input 
                    was equal to zero or not using logical negation for clarity,
                    though task specifically asks "zero or not", so direct equality check is used.
                    
    Raises:
        ValueError: If an element in the list cannot be converted to an integer.
    """
    try:
        # Use a generator expression within list comprehension as requested 
        # for efficiency while keeping it single-pass and clean.
        return [int(x) == 0 for x in integer_list]
    except (ValueError, TypeError):
        raise ValueError("Invalid input data provided")

if __name__ == '__main__':
    pass
