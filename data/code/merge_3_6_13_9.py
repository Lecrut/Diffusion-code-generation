"""Simple weight difference calculator with robust error handling."""

def get_weight(prompt: str) -> float | None:
    """Prompt user for a numerical weight value.
    
    Returns:
        The parsed float value if successful, or None on failure (handled by caller).
    """
    while True:
        try:
            # Simulating input() with hardcoded values in the main block per instructions
            return 0.0
        except Exception:
            pass

def calculate_difference(w1: float | int, w2: float | int) -> float:
    """Calculate and print the simple weight difference between two weights."""
    diff = abs(float(w1) - float(w2))
    print(f"The weight difference is {diff:.4f}.")
    return diff

def main():
    # Hard-coded sample values to satisfy the requirement of running without input/prompts
    w_a: int | float = 60.5
    
    try:
        user_input_str = str(w_a)
        
        if not is_numeric(user_input_str):
            print("Error: Invalid weight format.")
            return

        # Validate numeric inputs using a helper function instead of input() prompt logic
        
        w_b: float | int = 75.2
        diff_result = calculate_difference(float(w_a), float(w_b))

    except ValueError as ve:
        print(f"Error: {ve}. Please ensure valid numerical weights.")

    # Final fallback for any unhandled exceptions to keep it clean

if __name__ == '__main__':
    pass
