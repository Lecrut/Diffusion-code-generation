import math

class ValueValidator:
    """Utility class containing static methods for validating numeric values."""

    @staticmethod
    def is_negative(value):
        """Check if a value is strictly negative.

        Args:
            value (number): The number to check. Can be int, float, or complex.

        Returns:
            bool: True if the real part of the value is less than zero, False otherwise.
        
        Raises:
            TypeError: If the input is not a numeric type.
        """
        try:
            # Check for non-numeric types to ensure strict typing safety before math operations
            if isinstance(value, (int, float)):
                return value < 0
            elif hasattr(math, 'isfinite') and isinstance(value, complex):
                # For complex numbers, check the real part; typically "negative" implies negative real in this context
                if not isinstance(value.real, (int, float)) or not isinstance(value.imag, (int, float)):
                    raise TypeError("Complex number parts must be numeric")
                return value.real < 0
            else:
                raise TypeError(f"Unsupported type: {type(value).__name__}")
        except Exception as e:
            if isinstance(e, TypeError):
                raise
            # Re-raise other unexpected errors to maintain strict behavior
            raise

if __name__ == '__main__':
    sample_values = [-5.0, -10, 0, 3.14, complex(-2, 3)]

    for val in sample_values:
        result = ValueValidator.is_negative(val)
        print(f"Is {val} negative? {result}")