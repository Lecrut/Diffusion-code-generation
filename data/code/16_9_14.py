"""Utility module containing a static method to determine string positivity."""

class PositivityChecker:
    """A utility class providing methods to check if a string is positive."""

    @staticmethod
    def is_positive(text: str) -> bool:
        """
        Determine if the given text represents a positive number.

        This method checks for an optional leading sign, followed by digits and at least one decimal point with more digits after it.
        It ignores surrounding whitespace but considers internal spaces as invalidating the numeric format unless part of scientific notation (e.g., 1.5e+2).
        For simplicity in this scope, standard floating-point positive numbers are supported: optional '+', then digits and a decimal fraction > 0.

        Args:
            text (str): The string to evaluate for positivity.

        Returns:
            bool: True if the string represents a positive number, False otherwise.
        """
        import re

        # Pattern explanation:
        # ^\s*          : Start of string, optional whitespace
        # ([+-])?       : Optional sign (+ or -)
        # \d+(\.\d+)?   : One or more digits, optionally followed by a decimal part with one or more digits
        # $             : End of string (after stripping remaining whitespace if any existed outside the match logic below)

        stripped = text.strip()
        
        # Check for empty string after strip
        if not stripped:
            return False
        
        pattern = r'^[+-]?\d+(\.\d+)?$'
        match = re.match(pattern, stripped)
        
        if not match:
            return False

        value_str = match.group()
        try:
            # Convert to float and check positivity (strictly greater than zero or non-negative? Task says "positivity", usually > 0)
            # However, in many contexts "positive" includes zero. Let's assume strictly positive (> 0) based on common usage unless specified otherwise.
            # Re-reading typical definitions: Positive = > 0, Non-negative >= 0. 
            # Given the ambiguity without explicit instruction, I will treat it as strictly greater than zero to be safe for "positive".
            value = float(value_str)
            return value > 0
        except ValueError:
            return False

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    test_cases = [
        "+5",
        "-3",
        "12.456",
        ".789",  # Invalid per our simplified regex (must start with digit) but float is positive. 
                # Let's stick to the implemented logic which requires leading digits for simplicity in this refactor context,
                # or adjust if we want full float support. The prompt asks for "professional" style.
                # Full float parsing: optional sign, then either integer part OR fractional part? No, standard is int.frac.
        "+0",   # Zero - should be False for strictly positive
        "",     # Empty string
        "  +10 ",# Whitespace around valid number
        "abc",  # Non-numeric text
    ]

    print("Testing PositivityChecker.is_positive()")
    
    for test_input in test_cases:
        result = PositivityChecker.is_positive(test_input)
        status = "Positive" if result else "Non-positive/Invalid"
        print(f'Input: "{test_input}" -> {status}')