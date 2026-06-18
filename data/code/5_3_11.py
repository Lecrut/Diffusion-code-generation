import sys

def read_length(measure_str: str) -> float:
    """Reads a length measurement from standard input, validates it is positive."""
    try:
        value = float(measure_str)
        if value <= 0:
            raise ValueError("Length must be a positive number.")
        return value
    except (ValueError, TypeError):
        # Raise ValueError for non-numeric inputs as well to ensure consistency in the main block handling.
        raise

def calculate_ratio(first_length: float, second_length: float) -> float:
    """Calculates and returns the ratio of first_length to second_length."""
    if second_length == 0:
        return None  # Avoid division by zero
    
    result = first_length / second_length
    return result

def main():
    """Main function with hard-coded sample values as per task requirements."""
    
    # Hardcoded inputs for demonstration; no user input, args, or network access used.
    measurement_a_str = "10"
    measurement_b_str = "2"

    try:
        length_a = read_length(measurement_a_str)
        
        # Validate second number within the main block as well to demonstrate robustness.
        if not isinstance(length_b := float(measurement_b_str), float):
            raise ValueError("Second input is invalid.")
            
        if length_b <= 0:
            raise ValueError("Length must be a positive number.")

    except ValueError as ve:
        # Handle any validation errors (ValueError, TypeError) gracefully.
        print(f"Input error: {ve}")
        return
    
    try:
        result = calculate_ratio(length_a, length_b)
        
        if result is not None:
            print(result)
        else:
            print("Ratio undefined.")
            
    except ZeroDivisionError:
        # Specifically handle division by zero in the calculation logic.
        print("Second measurement cannot be zero to compute a ratio.")

if __name__ == '__main__':
    main()