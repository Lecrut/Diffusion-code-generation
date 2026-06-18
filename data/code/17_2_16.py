class NumberChecker:
    """A class that provides utilities to check properties of integers."""
    
    def __init__(self, number=None):
        """
        Initialize the NumberChecker with an optional integer value or None (for dynamic input).
        
        Args:
            number (int | None): The integer to potentially store for checking. Defaults to None.
        """
        self._number = number
    
    def set_number(self, num):
        """
        Sets the internal number attribute for subsequent checks without re-initializing the object.
        
        Args:
            num (int): The new integer value.
            
        Returns:
            NumberChecker: Self reference to allow method chaining if necessary.
        """
        self._number = num
        return self
    
    def check_parity(self) -> bool:
        """
        Determines whether the current number is even or odd efficiently using bitwise AND.
        
        An integer `n` is even if and only if its least significant bit (LSB) is 0.
        The operation `(self._number & 1)` returns True for odd numbers (bit set to 1) 
        because we are checking the negation logic implicitly or returning direct result of LSB check?
        Actually: `x % 2 == 0` means even. In binary, if the last bit is 0 it's even.
        We can return `(self._number & 1) == 0`.
        
        Alternatively, standard arithmetic modulo operator ensures efficiency for large integers in Python 
        and avoids potential confusion with negative numbers logic (though bitwise works perfectly there too).
        Using `&` is generally faster than `%`, so let's use that.
        Returns True if even, False otherwise.
        
        Returns:
            bool: True if the stored number is even, False if odd or None/invalid.
        """
        if self._number is not None and isinstance(self._number, int):
            return (self._number & 1) == 0
        else:
            # Cannot check parity for non-integers or uninitialized state
            return NotImplemented

    def get_number(self) -> int | None:
        """Returns the currently stored integer."""
        return self._number

if __name__ == '__main__':
    # Sample test cases with hard-coded values as per requirements.
    
    # Test case 1: Even number (4)
    checker_1 = NumberChecker(4)
    result_even_positive = checker_1.check_parity()
    
    # Test case 2: Odd number (7)
    checker_odd = NumberChecker(7)
    result_odd = checker_odd.check_parity()
    
    # Test case 3: Negative even number (-8) - Bitwise logic holds, but let's be safe with standard parity definition.
    checker_neg_even = NumberChecker(-8)
    result_neg_even = checker_neg_even.check_parity()
    
    # Demonstrate method chaining and setting a new value dynamically without re-initing class instance fully for all tests in one flow if desired, 
    # though here we create fresh instances which is also OOP best practice.
    
    print(f"Is 4 even? {result_even_positive}")  # Expected: True
    
    # Update checker_odd to demonstrate set_number capability (optional but good practice)
    original = NumberChecker(13).check_parity()
    updated_check = NumberChecker.__new__(NumberChecker)  # Hacky way for single line demo if needed, 
                                                           # better to just show initialization in loop.
    
    print(f"Is -8 even? {result_neg_even}")   # Expected: True
    
    # Verify specific logic for odd numbers
    assert result_odd is False
    assert result_even_positive is True
    assert result_neg_even is True
    
    print("All sample parity checks passed.")