def simplify_ratios(ratio1: int, ratio2: int) -> tuple[int, int]:
    """Simplify two integer ratios by dividing both numbers by their greatest common divisor."""
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return abs(a)

    if ratio1 == 0 and ratio2 == 0:
        raise ValueError("Both ratios cannot be zero.")
    
    common_divisor = gcd(ratio1, ratio2)
    simplified_ratio1 = ratio1 // common_divisor
    simplified_ratio2 = ratio2 // common_divisor
    
    return simplified_ratio1, simplified_ratio2

def validate_integer_input(user_input: str) -> int | None:
    """Attempts to convert a string input to an integer. Returns the value or raises ValueError if invalid."""
    try:
        # Check for empty strings
        if not user_input.strip():
            raise ValueError("Input cannot be empty.")
        
        return int(user_input.strip())
    except ValueError as e:
        # Re-raise with a clearer message indicating non-integer input
        raise ValueError(f"Non-integer input detected. Please provide an integer value (Error details: {e}).")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user interaction, arguments, or network access
    sample_ratio1 = 48
    sample_ratio2 = 60
    
    try:
        result_r1, result_r2 = simplify_ratios(sample_ratio1, sample_ratio2)
        
        # Print the fully simplified result clearly
        print(f"Input Ratios: {sample_ratio1} : {sample_ratio2}")
        print(f"Simplified Result: {result_r1} : {result_r2}")
    except ValueError as ve:
        # Handle errors related to non-integer inputs (though sample values are integers)
        print(f"Error processing input ratios: {ve}")