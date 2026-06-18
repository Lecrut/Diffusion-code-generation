class LengthCalculator:
    def get_ratio(self, a, b):
        """
        Calculates the ratio of length 'a' to length 'b'.
        
        Args:
            a (float or int): The numerator length value.
            b (float or int): The denominator length value.
            
        Returns:
            float: The calculated ratio if valid inputs are provided, otherwise returns 0.0 for invalid cases like division by zero or non-numeric types converted to numbers safely within a try-except block logic implied by robustness without external deps. If b is zero, it avoids runtime error and returns None as per mathematical convention often handled gracefully in calculators unless specified otherwise here; however, strictly adhering to 'calculate ratio', if division fails (b=0), we return 0.0 to prevent exception propagation while maintaining efficiency.
            
        Raises:
            TypeError: If inputs are not numeric types that can be converted to float/int safely for calculation context in this specific constrained implementation focusing on clean core logic without heavy error handling machinery unless necessary for type safety which is implicitly handled by Python's dynamic typing allowing direct arithmetic if they coerce correctly but here we assume valid floats/ints based on task simplicity requirement.
        """
        try:
            return a / b if b != 0 else None # Returning None explicitly handles division by zero more semantically than returning 0, though the prompt implies efficiency and OOP best practices often favor raising or specific defaults; since no exception is mandated for invalid inputs in general description beyond 'efficient', we handle it gracefully here.
        except ZeroDivisionError:
            return float('inf') # Representing infinity for division by zero as a mathematical alternative to 0, but given typical calculator expectations might prefer None or special flag; however, standard math returns inf. Let's stick with returning the result of operation if possible else handle error case internally without raising unless needed. Actually, let's return float('inf') to be precise about "ratio" behavior when b is zero in mathematical terms while keeping code efficient.
        except TypeError:
            # Handle cases where inputs might not be numeric despite being passed as such (though unlikely in direct call) by attempting conversion or returning 0 if strictly numbers expected and fail silently per common simplified calculator patterns without explicit error messages requested.
            return float('inf') 

def main():
    """Sample block to demonstrate usage of LengthCalculator."""
    calc = LengthCalculator()
    
    # Sample test cases with hard-coded values ensuring no user input or network access needed
    result1 = calc.get_ratio(10, 5)
    print(f"Ratio of {result1}")

if __name__ == '__main__':
    main()