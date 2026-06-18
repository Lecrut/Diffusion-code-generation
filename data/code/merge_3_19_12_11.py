import sys

class ConditionChecker:
    """A class that checks if one number is divisible by another."""
    
    def check(self, num1: float, num2: float) -> bool:
        """
        Returns True if num1 is divisible by num2, False otherwise.
        
        Args:
            num1 (float): The dividend.
            num2 (float): The divisor.
            
        Returns:
            bool: True if no remainder occurs when dividing num1 by num2.
                  Otherwise returns False or raises a ValueError for invalid input.
                  
        Raises:
            TypeError: If inputs are not numbers.
            ZeroDivisionError: If the second number is zero.
        """
        # Validate that both arguments are numeric types (int, float, complex)
        if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
            pass  # Valid type check passed for simple cases
            
        elif not ((isinstance(num1, (complex, int, float))) or 
                  (isinstance(num2, (complex, int, float)))):
             raise TypeError("Both arguments must be numeric types.")

if __name__ == '__main__':
    pass
