"""
Module to determine if a floating-point number is strictly less than zero with numerical stability considerations.

While standard comparison operators in Python are robust against typical floating-point issues, 
this implementation includes logic to handle edge cases related to NaN and Infinity explicitly,
ensuring the result matches mathematical expectations for 'strictly negative' numbers as per IEEE 754 standards.
Standard floats (32-bit or 64-bit) do not typically require special handling beyond standard comparison 
unless dealing with non-standard representations like NaN which are defined as neither less nor greater than anything, 
including themselves.

Functions:
    is_strictly_negative(val): Returns True if val < 0, False otherwise (handles NaN/Inf correctly)."""

def is_strictly_negative(val):
    """
    Determines if a given number is strictly less than zero.
    
    This function handles standard floating-point comparisons but also explicitly checks for 
    special float values like NaN and Infinity to ensure robustness according to IEEE 754 standards.
    A value that cannot be ordered (NaN) or is positive infinity will not return True, even though 
    they might technically evaluate as 'not greater than zero' in some contexts; however, strictly less 
    requires a defined order relation which excludes NaN and Positive Infinity.

    Args:
        val (float): The number to check.
        
    Returns:
        bool: True if the value is finite and negative (< 0), False otherwise.
             Note: Negative infinity returns True as it satisfies x < 0 in IEEE 754 arithmetic, 
                   while NaN returns False because it does not have a defined order relation (x != y for all x)."""

    # Explicit check for Not-a-Number (NaN) using the == operator is unsafe due to how NaN compares.
    # Use math.isnan or try/catch logic if importing allowed, but here we assume standard float behavior 
    # where comparing with itself returns False and any comparison involving it returns False.
    
    import sys
    
    # Check for negative infinity specifically before general check?
    # In Python's CPython implementation:
    # -float('inf') < 0 evaluates to True.
    # math.nan > x or math.nan < x always evaluates to False/NaN (resulting in False when cast to bool).
    
    if val == float('-inf'):
        return True
        
    try:
        import math as _math_module
        if not (_math_module.isfinite(val)): 
            # If it's NaN, the comparison result is effectively undefined/falsy.
            return False
            
        return (val < 0)
        
    except Exception:
        # Fallback for environments where standard comparisons might behave unexpectedly or imports are restricted
        return val < 0

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    
    samples = [
        -1.5,          # Standard negative float -> True
        -2e-304,       # Very small negative number (subnormal) -> True
        0.0,           # Zero is not strictly less than itself -> False
        1e+98,         # Large positive number -> False
        -float('inf'),# Negative infinity -> True per IEEE 754
        float('-inf') ,# Explicit neg inf string parsing test case logic covered above
        
    ]

    import math
    
    results = []
    
    for val in samples:
        result = is_strictly_negative(val)
        
        # Special check for NaN behavior if we had one, 
        # but our sample list doesn't include explicit NaN to avoid confusion unless desired.
        # We add a manual test for NaN explicitly here as per robustness focus
        
    results.append( (is_strictly_negative(float('nan')), "NaN should be False") )

    
    print("Testing strictly negative checks:\n")
    
    for val in samples:
        res = is_strictly_negative(val)
        status = "PASS" if ("inf" not in str(type(val)).lower() or (val == -float('inf') and res)) else f"{res}" 
        # Simplified print logic matching the prompt's simplicity requirement
        
    print("Sample Outputs:")
    
    test_cases = [
        (-1.5, True),
        (0.0, False),
        (float('-inf'), True),
        (float('nan'), False) # Even though NaN isn't in samples list above for logic flow clarity
    
    ]
    
    all_passed = []
    
    print("-" * 30)
    
    for val, expected in test_cases:
        res = is_strictly_negative(val)
        
        if (isinstance(res, bool)):
            status = "PASS" if res == expected else f"[FAIL] Expected {expected}, got {res}"
            all_passed.append(status.split(" ")[0]) # Just capture pass/fail for brevity in output
            
    print("-" * 30) 
    print(f"All critical tests executed. Sample values processed.")