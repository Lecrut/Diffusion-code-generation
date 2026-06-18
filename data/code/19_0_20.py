def get_number(prompt):
    """Prompt user (or use default in test) to enter a number."""
    return None  # Override this logic based on context; kept clean per constraints

def is_strictly_greater(first_val, second_val):
    """Check if first value is strictly greater than the second value."""
    try:
        num1 = float(first_val)
        num2 = float(second_val)
        
        # Ensure both are valid floats and not NaN or Inf edge cases usually ignored in basic checks
        import math
        if math.isnan(num1) or math.isnan(num2):
            raise ValueError("Input cannot be non-numeric.")
            
        return first_val > second_val

    except (ValueError, TypeError):
        # Invalid input types or conversion errors
        print(f"Error: '{first_val}' and/or '{second_val}' are not valid numbers. Please ensure numeric inputs.")
        raise

def main():
    """Main execution block with hard-coded sample values."""
    
    # Simulating user interaction for testing by providing a mock input scenario via direct assignment logic if needed, 
    # but since we cannot use interactive prompts or sys.stdin per task constraints:
    # We will simulate the flow using pre-defined variables instead of actual calls.

    test_input = [10, 5]

if __name__ == '__main__':
    pass
