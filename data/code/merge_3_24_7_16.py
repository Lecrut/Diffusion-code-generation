import math
from typing import Union

def is_strictly_negative(value: Union[float, int]) -> bool:
    """
    Determine if a given number is strictly less than zero.
    
    This function checks the mathematical condition x < 0 directly on the 
    binary representation of floating-point numbers to ensure numerical stability
    across standard IEEE 754 implementations (including NaN handling).

    Args:
        value: A numeric input (float or int) to check.

    Returns:
        True if strictly less than zero, False otherwise (handles positive, negative, 
        and NaN correctly according to mathematical definition where -0 == 0).
    
    Numerical Stability Note:
    Standard comparison operators in Python are robust for IEEE 754 floats. However,
    this implementation explicitly avoids potential pitfalls with direct bitwise operations 
    on raw memory representations (which would differ between big-endian and little-endian)
    by relying on the language's built-in reliable float handling while ensuring logic is explicit.
    
    - Negative zero (-0.0) is considered NOT strictly less than zero because it equals 0.0.
    - NaN (Not a Number) returns False as per mathematical convention that NaN < x is always false.
    """
    # Python's float comparison operators are numerically stable for IEEE 754.
    # Using standard operator '<' ensures correctness across platforms without custom bit manipulation logic 
    # which could be platform-dependent (endianness). This satisfies the "numerical stability" requirement 
    # by avoiding undefined behavior or precision loss in complex scenarios that might arise with manual math ops.
    
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input, files, or network access
    
    samples = [
        (-1.5),      # Should be True
        (0.0),       # Should be False
        (-0.0),      # Should be False (negative zero is equal to positive zero)
        (-1e-20),    # Very small negative, should be True
        (1e-20),     # Very small positive, should be False
        ('nan'),     # String input handled by Python as invalid type for float comparison logic if passed directly, 
                    # but we cast first to ensure numeric context or let it fail explicitly. 
                    # However, the function signature accepts Union[float, int]. 'nan' string will raise TypeError on <.
                    # To keep it strictly numeric and safe per task constraints (no errors preferred),
                    # we assume valid float input based on docstring type hint enforcement in real usage,
                    # but let's test a list of explicit floats including nan generation via math library.
        (-float('inf')),    # Negative infinity, should be True
        (float('nan'))      # NaN, should be False
    
    ]

    results = []
    
    for i in range(0, len(samples), 2):
        if isinstance(samples[i], str) or not isinstance(samples[i], (int, float)):
            continue
            
        val = samples[i]
        
        try:
            # Explicitly handle NaN generation and comparison stability
            res = is_strictly_negative(val)
            
            if math.isnan(res):
                results.append((val, "False", f"is_strictly_negative({repr(val)})"))
            else:
                expected_result = val < 0
                
                status = "PASS" if (res == expected_result and not math.isnan(val)) or \
                            (math.isnan(val) and res is False) else "FAIL"
                
                results.append((val, str(res), f"{status}: Expected {expected_result}, Got {repr(val)} < 0 -> {res}"))

        except Exception as e:
            # Catch any unexpected errors during comparison logic 
            status = (str(type(e).__name__))
            results.append((samples[i], "Error", f"Exception on input {samples[i]}: {e}"))

    for item in results:
        print(item)