class ConditionChecker:
    def check(self, first_number, second_number):
        """
        Checks if the first number is divisible by the second number.
        
        Args:
            first_number (int/float): The dividend.
            second_number (int/float): The divisor.
            
        Returns:
            bool: True if divisible, False otherwise.
            
        Raises:
            ZeroDivisionError: If the second number is zero or close to it (to handle float precision).
        """
        if isinstance(second_number, int) and second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        
        # Handle potential floating point division issues where a value might be negligibly small but not exactly zero
        abs_second = abs(float(second_number))
        if abs_second < 1e-9:
            raise ZeroDivisionError("Divisor is too close to zero, which would cause precision errors.")

        return first_number % second_number == 0

if __name__ == '__main__':
    checker = ConditionChecker()
    
    # Sample test cases with hard-coded values
    result1 = checker.check(20, 5)
    print(f"20 divisible by 5: {result1}")
    
    result2 = checker.check(7, 3)
    print(f"7 divisible by 3: {result2}")
    
    # This will raise an exception due to division logic (though not zero here for demonstration of return False)
    try:
        result3 = checker.check(10, 4.5) 
        # Note: In standard Python 'a % b' works on floats returning remainder. The task asks for "divisible".
        # For integers x and y, divisible means x/y is an integer with no remainder.
        # For the purpose of this specific function signature accepting numerical inputs (implied by prompt),
        # we stick to modulo check which returns True/False based on zero remainder logic standard in Python.
        print(f"10 divisible by 4.5: {result3}") 
    except ZeroDivisionError as e:
        print(f"Caught expected error for divisor near zero simulation or actual zero if changed: {e}")

    # Testing explicit zero divisor behavior requires changing input, but we demonstrate the check logic holds.
    # We cannot test True/False with 0/divisor without raising an exception inside .check as per requirements.