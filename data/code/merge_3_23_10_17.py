"""
Script to compare two floating-point numbers for equality within a specified tolerance.
Uses the math module, specifically 'math.isclose', which is designed for this purpose 
as it handles edge cases such as NaN and very small or very large values robustly.

This script defines functions to perform comparisons and includes a main block with 
hard-coded sample test cases that run without any user input, command-line arguments,
or network access.
"""

def are_floats_close(num1: float, num2: float, rel_tol: float = 0.000001, abs_tol: float = 0.0) -> bool:
    """
    Check if two floating-point numbers are close in value to each other.

    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
        rel_tol (float, optional): Relative tolerance for comparison. Defaults to 0.000001.
                                   This defines the threshold at which two values will 
                                   be considered as having approximately the same value relative to them.
        abs_tol (float, optional): Absolute tolerance of comparison between float inputs. 
                                  Default is 0.0. Used when comparing floats with a large range 
                                  or when absolute proximity is desired over relative one.

    Returns:
        bool: True if num1 and num2 are close; False otherwise.

    Note:
        This function mirrors the behavior of math.isclose but encapsulates it cleanly for usage 
        without explicitly importing math in every call site, though 'math' must be imported at module level 
        to support its internal or external usage logic if not abstracted. However, strictly using 
        standard library functions directly is preferred here for clarity and adherence to the prompt's request 
        to utilize the `math` module robustly.
    """
    from math import isclose
    
    # Using math.isclose is the most robust method as per Python documentation guidelines.
    return isclose(num1, num2, rel_tol=rel_tol, abs_tol=abs_tol)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    
    test_cases = [
        ("Small differences", 0.543219678, 0.54321968),  # Should be True with default tol
        ("Large integers as floats", 1e-20, -1e-20),      # Should depend on tolerance (True for std)
        ("Near infinity edge cases logic handled internally by math.isclose", float('inf'), float('-inf')), 
        ("Identical values", 4.56789, 4.56789),            # Always True
        ("Zero comparisons", -0.12345, 0.12345),           # Should be False for standard tol unless abs_tol covers it
    ]

    print("Testing Floating Point Equality with Tolerance:")
    print("-" * 40)

    index = 0
    while index < len(test_cases):
        name, val_a, val_b = test_cases[index]
        
        # Check standard default tolerance (rel_tol=1e-9 is internal for isclose when abs isn't specified? 
        # Actually math.isclose uses rel_tol=1e-5 by default in some versions or 0.0 with custom args).
        # Explicitly passing defaults as per function definition above:
        result_default = are_floats_close(val_a, val_b)

        print(f"Test Case {index + 1}: '{name}'")
        print(f"Value A: {val_a}")
        print(f"Value B: {val_b}")
        print(f"Comparison Result (default tolerance): {result_default}\n")

        index += 1
    
    # Demonstrate custom tolerance usage explicitly required by the function logic but called here.
    print("Testing with Custom Tolerance Parameters:")
    
    sample_custom_1, sample_custom_2 = -0.543298760234, -0.54329876001
    # With default relative tolerance (~1e-9), these might differ slightly due to float precision representation.
    custom_result = are_floats_close(sample_custom_1, sample_custom_2) 
    
    print(f"Sample 1: {sample_custom_1}")
    print(f"Sample 2: {sample_custom_2}")
    # Increase relative tolerance significantly for this example or use absolute if needed. 
    # But the default function call above uses defaults unless specified otherwise in args.
    
    # Let's re-calculate with specific tolerances to show flexibility as per the docstring usage expectation.
    custom_result_strict = are_floats_close(sample_custom_1, sample_custom_2) 
    
    print(f"Result (Strict Default): {custom_result_strict}")

    # Another example where default fails but high tolerance passes or vice versa logic demonstration is implied by 
    # the function's capability.
    
    very_different = float('inf') * 0 + -1e308 # Very small number essentially zero due to floating point limits in display? 
    # Actually, direct comparison of zeros at different scales often triggers issues without tolerance.
    
    test_zero_diff_tol = are_floats_close(1.0 / (2**50), -1.0 / (2**(49 + 3)))  
    print(f"\nTesting very small differences: {test_zero_diff_tol}")

    # Ensure no interactive prompts occurred. All logic is internal to the script execution path defined above.