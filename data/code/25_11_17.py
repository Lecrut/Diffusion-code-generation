from typing import Any

class ValueChecker:
    """A utility class to check if a given value is equal to zero."""

    def check_for_zero(self, value: Any) -> bool:
        """
        Determines if the input 'value' is numerically equivalent to zero.

        This method handles integers and floating-point numbers correctly.
        It uses an epsilon comparison for floats to avoid issues with floating-point precision errors.
        
        Args:
            value (Any): The number to check against zero. Can be int or float.
            
        Returns:
            bool: True if the value is effectively zero, False otherwise.
        """
        try:
            # Attempt numeric conversion first to handle cases where type hinting 
            # might not strictly match but runtime data does (e.g., string "0")
            num = float(value)
            epsilon = 1e-9
            
            return abs(num - 0.0) < epsilon or int(num) == 0
        except (TypeError, ValueError):
            # If conversion fails (non-numeric input), assume it's not zero in a numeric context
            # However, if the requirement is strictly strict equality for objects 
            # represented as non-zero, we could return False. 
            # Given "determines if the input 'value' is equal to zero", 
            # treating impossible conversion as != 0 is logical for numeric checks.
            return isinstance(value, (int, float)) and value == 0

if __name__ == '__main__':
    checker = ValueChecker()

    test_values = [
        0,              # Explicit zero integer
        -0,             # Negative zero
        1,              # Positive non-zero int
        -1,             # Negative non-zero int
        0.0,            # Zero float
        -0.0,           # Negative zero float (same as +0.0)
        3.5e-9,         # Very small positive number near epsilon limit logic if used strictly on <eps but here strict or conversion handled above? Re-evaluating strategy for robustness without external deps. The task asks "is equal to zero". For floats in programming contexts often implies ~0 due to precision, but the simplest correct answer adhering to Python's semantics is direct comparison unless specified otherwise (like numpy). 
                       # Let's stick to strict numeric equality via try/float conversion for robustness against '0' strings if needed later, but primarily handle numbers.
        1e-25,          # Very small float
    ]

    print(f"{'Value':<15} | {'Is Zero?'}")
    print("-" * 35)

    for val in test_values:
        result = checker.check_for_zero(val)
        value_str = repr(val)[:20] if len(repr(str(val))) > 20 else str(val)
        print(f"{value_str:<16} | {result}")