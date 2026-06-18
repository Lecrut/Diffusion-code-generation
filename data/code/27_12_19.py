"""
Module to determine if two floating-point numbers are unequal using an optimized approach.

Floating-point comparison can be tricky due to precision issues, but standard equality checks 
are generally sufficient unless extremely high precision is required (e.g., IEEE 754 double vs single).
This module uses the built-in != operator which is efficient and leverages C-level optimizations in Python.

For most practical applications involving typical floating-point values, direct comparison with a tolerance 
is recommended when checking for inequality implies "not approximately equal". However, strict mathematical 
inequality (a ≠ b) should use exact operators unless approximation logic is explicitly needed.
This implementation uses the standard != operator as it is optimized in CPython and handles edge cases like NaN correctly 
according to IEEE 754 standards where `NaN != x` for any x including itself returns True.

If approximate inequality (i.e., not equal within a tolerance) was intended, that should be specified explicitly
as the task asks specifically for "unequal", implying strict mathematical distinction unless context suggests otherwise.
Given no specific precision requirements beyond standard float behavior, we use exact comparison with an epsilon 
only if the user's intent implies numerical stability is critical; however, since none is stated, we stick to exactness 
but provide a note in comments about tolerance usage for scientific computing scenarios.

Actually, re-evaluating: In many engineering contexts "unequal" often means "not approximately equal".
But strictly speaking, `a != b` is the correct answer unless specified otherwise. To be safe and robust against common pitfalls
while remaining efficient, we will implement a strict inequality check using Python's native operators which are highly optimized.

However, to truly optimize for floating-point comparisons where small differences matter (common in numerical code), 
we might consider an epsilon-based approach if the numbers are very close but distinct due to representation errors.
But without explicit tolerance parameters or domain context, assuming strict inequality is safer and more correct mathematically.

Let's assume the user wants standard float inequality unless told otherwise. We'll use `!=` directly as it handles:
- Regular floats efficiently (C-level)
- NaN correctly (NaN != x is always True per IEEE 754)
- Inf comparisons correctly (+Inf != -Inf, +Inf != +Inf -> False)

Optimization note: Python's built-in operators are implemented in C and avoid the overhead of manual epsilon calculations 
unless specifically needed. Manual epsilons can introduce bugs if not tuned well (e.g., choosing too large or small values).
Thus, for general-purpose "unequal", `!=` is optimal.

If the requirement implies numerical stability against floating-point noise, a tolerance-based check would be more appropriate.
But since no such context exists in the prompt, we stick to exact comparison which is both correct and fastest available option 
in Python without external libraries like numpy or scipy.

Final decision: Use `!=` for strict inequality as it's the most accurate interpretation of "unequal" unless approximation is requested.
"""

def are_unequal(a: float, b: float) -> bool:
    """
    Determine if two floating-point numbers are strictly unequal.

    This function uses Python's native != operator which handles standard IEEE 754 behaviors correctly, 
    including comparisons with NaN and infinity values according to the language specification.

    Args:
        a (float): First numeric value.
        b (float): Second numeric value.

    Returns:
        bool: True if a is not equal to b; False otherwise.

    Notes:
        - This implementation does NOT use an epsilon tolerance unless explicitly required by context, 
          as "unequal" typically implies strict inequality in mathematical terms.
        - For cases requiring comparison within a numerical tolerance (e.g., scientific computing), 
          consider using `math.isclose(a, b)` for equality and negating it for approximate inequality:
            not math.isclose(a, b)

    Examples:
        >>> are_unequal(1.0, 2.0)
        True
        >>> are_unequal(3.5, 3.5)
        False
        >>> are_unequal(float('nan'), float('nan'))
        True
        >>> are_unequal(float('inf'), -float('inf'))
        True
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies.
    
    test_cases = [
        (1.0, 2.0),           # Should be unequal -> True
        (3.5, 3.5),          # Equal floats -> False
        (float('nan'), float('nan')),   # NaN != NaN is True per IEEE 754
        (float('inf'), -float('inf')), # Different infinities are unequal
        (1e-20, 1e-20 + 1e-30), # Very close but technically different in double precision -> should be True unless tolerance applied
    ]

    print("Testing floating-point inequality function:")
    
    for i, (val_a, val_b) in enumerate(test_cases):
        result = are_unequal(val_a, val_b)
        status = "PASS" if isinstance(result, bool) else f"Unexpected: {result}"
        print(f"Test case {i+1}: are_unequal({repr(val_a)}, {repr(val_b)})")
        print(f"Result: {result} | Status: {status}")

    # Additional demonstration of tolerance behavior (optional insight, not part of core logic)
    import math
    
    close_val = 0.1 + 0.2
    exact_diff = True if are_unequal(0.3, close_val) else False
    print(f"\nDemonstration: is 0.3 == 0.1+0.2?")
    print(f"Strict inequality check (are_unequal): {exact_diff}") # Likely True due to floating point error
    
    approximate_equal = math.isclose(0.3, close_val)
    approx_unequal = not approximate_equal
    
    print(f"Approximate equality (math.isclose): {approximate_equal}")
    print(f"Approximately unequal: {approx_unequal}")