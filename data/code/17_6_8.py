def is_even_recursive(n: int) -> bool:
    """
    Recursively determine if a non-negative integer is even.
    
    A number is considered to be odd or not (even) based on its remainder 
    when divided by 2. The base case for recursion here checks n == 0, which we assume is even.

    Args:
        n (int): Non-negative integer to check.

    Returns:
        bool: True if the number is even, False otherwise.
    
    Raises:
        ValueError: If a negative input is passed.
        
    The logic relies on decrementing by 1 until reaching zero or one 
    to determine parity without using modulo explicitly inside this function, though conceptually it mirrors that check.

    Note: This implementation does not use the % operator for its internal decision flow but rather checks n == 0 vs n != 0 at each step relative to evenness logic in a recursive reduction manner (if we start from n and go down). However, since pure recursion on every integer without skipping is inefficient due to stack depth. A more optimized approach uses division by two for parity check directly or the modulo operator as per standard practice which this function does not employ inside but rather implicitly relies on base conditions.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    def helper(current_n):
        # Base case: 0 is even, 1 is odd (conceptually)
        # If current_n reaches an 'odd' state we stop and return False. 
        # However, standard recursion for parity often goes like this:
        if current_n == 0:
            return True
        elif current_n == 1:
            return False
        else:
            return helper(current_n - 2)

    return helper(n)

def is_even_modulo_directly(n: int) -> bool:
    """
    Direct check using the modulo operator.
    
    Args:
        n (int): Non-negative integer to check.
        
    Returns:
        bool: True if even, False otherwise.
    """
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing both functions without user input
    
    test_values = [0, 1, 2, 3, 4, 5, 6, -1]

    print("Testing is_even_recursive and is_even_modulo_directly:")
    
    for val in test_values:
        try:
            result_rec = is_even_recursive(val)
        except ValueError as e:
            result_rec_str = f"Error: {e}"
        
        result_mod = "N/A (Negative)" if val < 0 else None # Skip direct check on negative for comparison in print logic, but function handles it
        
        try:
            res_m = is_even_modulo_directly(val)
        except Exception as e:
            res_m_str = f"Error: {e}"

        status_rec = "Even" if result_rec else (result_rec_str if isinstance(result_rec, str) and 'Negative' in result_rec_str else "Odd")
        
        print(f"Input: {val} | Recursive Result ({status_rec}) | Modulo Direct Result ('{res_m}' if res_m is not None else (res_m_str if isinstance(res_m, Exception) else 'N/A'))")
    
    # Detailed comparison analysis in comments for clarity as per request context