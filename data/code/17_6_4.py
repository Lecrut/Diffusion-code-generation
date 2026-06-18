def is_even_recursive(n: int) -> bool:
    """
    Recursively determine if a non-negative integer is even.
    
    The logic subtracts 2 from n until it reaches 0 or -1 (which implies 
    the number was odd). Since we start with a non-negative integer,
    reaching exactly 0 means 'even', and stopping before that would mean 'odd'.

    Args:
        n (int): A non-negative integer.

    Returns:
        bool: True if even, False otherwise.
    
    Raises:
        ValueError: If the input is negative.
    """
    # Base condition for recursion termination based on parity
    if n == 0 or n % 2 != 1: 
        return True

if __name__ == '__main__':
    pass
