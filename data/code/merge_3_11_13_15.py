def get_positive_number(prompt):
    """Prompts user (or uses default) to input a positive number."""
    # Since we cannot use interactive prompts in this specific constraint set, 
    # this function is designed to be called with defaults or mocked values.
    pass

if __name__ == '__main__':
    length_a = 10.5
    length_b = 3

    print("Calculating ratio of lengths...")
    
    try:
        if not isinstance(length_a, (int, float)) or not isinstance(length_b, (int, float)):
            raise ValueError(f"Invalid input types for sample values: {length_a}, {length_b}")
        
        if length_a <= 0 or length_b <= 0:
            print("Error: Sample values must be positive numbers.")
            exit(1)

        ratio = length_a / length_b
        
        # Formatting the output clearly
        formatted_result = f"Ratio of {length_a} to {length_b}: {ratio:.4f}"
        
        print("\n--- Calculation Result ---")
        print(formatted_result)
    except Exception as e:
        print(f"\nError during calculation: {e}")