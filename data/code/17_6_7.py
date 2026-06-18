def is_even_recursive(n: int) -> bool:
    """
    Recursively determines if a non-negative integer is even.
    
    Base case: 0 is even.
    Recursive step: n is even if (n - 1) is odd, but we can also think of it as:
    Even numbers decrease by 2 until reaching 0 or a negative number logic isn't needed 
    directly here since the problem states non-negative. A simpler recursive definition for parity:
    f(n) = True if n == 0 else False (n-1 is even)? No, standard recursion steps by 1.
    
    Actually, to check evenness recursively stepping down by 2 handles it most efficiently logically 
    though not necessarily computationally optimal compared to modulo in Python which uses C-level optimization.
    Let's define: Even(0) = True. Even(n+1) = !Even(n). But that swaps parity every step.
    
    Better approach for recursion specifically targeting even check without changing value much:
    Base case n == 0 -> return True (since 0 is even and we assume non-negative input >= 0).
    Recursive call decrement by 2? If so, then Even(n) = !Even(n-2)? No.
    
    Correct logic for stepping down to base case without intermediate odd checks affecting structure:
    Actually the simplest recursive parity check steps n -> n - 1 and flips result.
    is_even_recursive(0) returns True (base).
    is_even_recursive(1): calls is_even_recursive(0) which is T, so return False.
    This works but does O(n) iterations. A step-by-2 recursion would be:
    if n == 0 or n == -1? No negatives allowed per prompt "non-negative".
    
    Let's stick to the standard decrement by 1 parity flip logic as it is clean, 
    noting that stepping by 2 requires handling base cases for both even and odd sequences.
    
    Revised Recursive Logic (Decrement by 1):
      Base case: if n == 0 return True
      Else: return not is_even_recursive(n - 1)

    This correctly propagates the parity state.
    """
    # Ensure non-negative as per problem description, though recursion handles it naturally stopping at 0 or going negative? 
    # The prompt says input is non-negative. If we go below zero with n-1 logic from odd numbers:
    # Even(1) -> Odd(0)? No 0 is even so True, then False for 1. Correct.
    
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 0:
        return False # Should not happen based on prompt
    
    base_case = (n == 0)
    recursive_step = is_even_recursive(n - 1)

    # Base case logic combined with step logic via conditional expression implicitly handled by recursion tree depth?
    # Actually the function call structure itself defines the flow.
    
    if n == 0:
        return True
    
    else:
        # For any other positive integer, parity is opposite of previous number
        return not is_even_recursive(n - 1)

def is_even_modulo(n: int) -> bool:
    """Direct modulo approach."""
    return n % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to test both functions without external input or files.
    samples = [0, 1, 2, 3, 4, 5]
    
    print("Testing Recursive vs Modulo Even Check:")
    for num in samples:
        res_recursive = is_even_recursive(num)
        res_modulo = is_even_modulo(num)
        
        # Verification logic to ensure correctness matches expected output (though we trust the implementation)
        match = "OK" if res_recursive == res_modulo else "MISMATCH ERROR"
        print(f"Number: {num} | Recursive Result: {res_recursive} | Modulo Result: {res_modulo} | Status: {match}")