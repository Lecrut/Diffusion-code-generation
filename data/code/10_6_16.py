import sys

def temperature_comparator(t1: float | int, t2: float | int) -> None:
    """
    Generator function that yields a string describing the comparison 
    between two temperatures.
    
    Args:
        t1 (float|int): First temperature value.
        t2 (float|int): Second temperature value.
        
    Yields:
        str: A formatted message indicating which is warmer and by how much.
    """
    diff = t1 - t2
    
    if abs(diff) < 0.0001:  # Handle floating-point precision issues for equality check
        yield f"{t1} and {t2} are equal (difference is negligible)."
        return

    warmer_temp, cooler_temp = None, None
    
    if diff > 0:
        warmer_temp, cooler_temp = t1, t2
        direction = "warmer"
    else:
        warmer_temp, cooler_temp = t2, t1
        direction = "cooler"

    magnitude = abs(diff)
    
    # Format the message clearly stating who is warmer by how much
    yield f"{warmer_temp} is {direction} than {cooler_temp} by {magnitude:.2f} degrees."

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input
    
    test_cases = [
        (85.0, 70.0),   # Example: 1st is warmer
        (-5.0, -5.0),   # Exact match with epsilon tolerance
        (23.4, 23.6),   # Reverse case: 2nd is warmer
    ]

    for t_a, t_b in test_cases:
        print(f"\n--- Comparing {t_a} and {t_b} ---")
        results = list(temperature_comparator(t_a, t_b))
        for result in results:
            print(result)