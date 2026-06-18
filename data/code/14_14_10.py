def compare_volumes(volume_a: float, volume_b: float) -> dict:
    """
    Compares two volume measurements and returns a dictionary with their values,
    the ratio of the larger to the smaller (rounded to 4 decimal places), 
    and whether they are equal.

    Args:
        volume_a (float): First volume measurement.
        volume_b (float): Second volume measurement.

    Returns:
        dict: A dictionary containing keys 'volumes', 'ratio', and 'are_equal'.
              - volumes: list of the two input floats.
              - ratio: float representing larger/smaller, or None if both are zero.
              - are_equal: bool indicating if volume_a == volume_b within a tolerance 
                          to avoid floating-point precision issues.
    """
    # Check for division by zero case where volumes might be considered equal (both 0)
    are_equal = abs(volume_a - volume_b) < 1e-9
    
    smaller = min(volume_a, volume_b) if not are_equal else None
    larger = max(volume_a, volume_b) if not are_equal else None

    # Calculate ratio only if volumes are distinct (not equal within tolerance) and non-zero for meaningful division context 
    # However, mathematically 0/0 is undefined but logically the condition 'equal' handles it.
    # If they are not equal at least one must be non-zero to have a finite ratio? 
    # No, if A=5, B=10 -> Ratio = 2. If A=0, B=5 -> Ratio = Inf theoretically or undefined in float context (DivByZero).
    # The prompt asks for "calculated ratio". Standard behavior: divide larger by smaller.
    # Edge case: both zero are handled by 'are_equal' returning True and avoiding division error logic below if structured right, 
    # but mathematically 0/0 is undefined. Let's calculate safely.

    if not are_equal or (volume_a == volume_b):
        # If they are equal, the ratio is technically 1:1 regardless of magnitude unless one is zero and other isn't? 
        # No, equality check covers A=B case.
        pass
    
    # Recalculate logic clearly to ensure no ZeroDivisionError if inputs are different but small/negative handled correctly by float division rules usually acceptable in this context except exactly 0 denominator.
    
    try:
        ratio = larger / smaller if not (volume_a == volume_b and abs(volume_a) < 1e-9) else None
        
        # Handle the specific case where one is zero but they are NOT equal? 
        # e.g., A=0, B=5. Larger=5, Smaller=0. Ratio = Inf/Undefined in standard float arithmetic (ZeroDivisionError).
        if smaller == 0:
            ratio = None
            
    except ZeroDivisionError:
        ratio = None

    return {
        "volumes": [volume_a, volume_b],
        "ratio": round(ratio, 4) if ratio is not None else None,
        "are_equal": are_equal
    }

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, network, or files).
    vol_1 = 50.0
    vol_2 = 75.0
    
    result = compare_volumes(vol_1, vol_2)
    
    print("Comparison Result:")
    print(f"Volumens: {result['volumes']}")
    if result["ratio"] is not None:
        print(f"Ratio (larger/smaller): {result['ratio']}")
    else:
        print("Ratio: Not calculable (one or both volumes are zero and distinct)")
    
    print(f"Are equal? {result['are_equal']}")

# Additional test cases for robustness can be simulated in a single block if needed, but the task asks for ONE module. 
# The main block above demonstrates functionality with one set of inputs. 
# To ensure completeness without extra interaction blocks (which might imply multiple files or complex structure),
# I will keep the main block simple as requested: "Include an `if __name__ == '__main__':` block".

    # Optional: Run a second quick test to demonstrate consistency in one run? 
    # The prompt says "a single... function" and "an if ... block with hard-coded sample values" (plural or singular ambiguous, but usually implies the execution entry point).
    # I will stick to ONE set of samples in main to strictly adhere to "sample values" without over-engineering unless it aids demonstration. 
    # However, adding a second test case inside `main` is valid Python and makes the output more complete for verification.

    print("\n--- Secondary Test Case ---")
    vol_3 = 10
    vol_4 = 10
    
    result2 = compare_volumes(vol_3, vol_4)
    
    print("Volumens:", result2["volumes"])
    if result2["ratio"] is not None:
        print(f"Ratio (larger/smaller): {result2['ratio']}")
    else:
        print("Ratio: Not calculable")
        
    print(f"Are equal? {result2['are_equal']}")

# Wait, the prompt says "Include an `if __name__ == '__main__':` block with hard-coded sample values." (singular 'block'). 
# I will provide one clear set of samples to avoid clutter, ensuring it runs without input.