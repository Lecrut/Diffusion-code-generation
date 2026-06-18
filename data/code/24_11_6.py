class NumberChecker:
    def check_negativity(self, value):
        """
        Determines if the input value is negative.
        
        Args:
            value (int | float): The number to check.
            
        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Sample test cases with hard-coded values
    samples = [
        -5,      # Negative integer
        0,       # Zero (not negative)
        3.14,    # Positive float
        -2.718,  # Negative float
        None     # Expected to raise TypeError as per standard Python behavior for comparison with mixed types unless handled explicitly; 
                 # However, the task asks for efficiency and clean OOP without extra constraints on type safety beyond negativity check.
                 # Standard < operator raises TypeError for incompatible types like int vs None/str in some contexts but works if both are numeric or comparable.
                 # To ensure robustness while staying "clean", we let Python's native comparison handle it, which is efficient and idiomatic.
    ]

    print("Testing NumberChecker.check_negativity:")
    for sample in samples:
        try:
            result = checker.check_negativity(sample)
            status = f"Value {sample} -> Negative? {result}"
        except TypeError as e:
            # This handles cases where the type is not directly comparable (e.g., None, string)
            status = f"Error checking {type(sample).__name__}: {str(e)}"

    print(statuses if (statuses := [f"{s} -> Negative? {checker.check_negativity(s)}" for s in samples]) else "No output")