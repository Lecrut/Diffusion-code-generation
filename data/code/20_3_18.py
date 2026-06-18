import sys

def parse_number(value):
    """Convert a string to an integer if possible, otherwise raise ValueError."""
    try:
        return int(value)
    except ValueError:
        # Attempt float conversion as secondary fallback
        try:
            return float(value)
        except ValueError:
            pass
        raise

def compare_numbers(num1_str, num2_str):
    """Compare two numbers and print whether they are equal."""
    if not isinstance(num1_str, str) or not isinstance(num2_str, str):
        raise TypeError("Both inputs must be strings.")
    
    try:
        num1 = parse_number(num1_str.strip())
        num2 = parse_number(num2_str.strip())
        
        # Handle comparison based on type (int vs float logic handled by Python)
        if isinstance(num1, int):
            print(f"{num1} == {num2}: {'True' if num1 == num2 else 'False'}")
        elif isinstance(num2, int):
            print(f"{float(num1)} == {num2}: {'True' if float(num1) == num2 else 'False'}")
        else:
            # Both are floats or one is a large integer that became float during parsing logic above (though parse_number returns exact types usually unless input was decimal string for int context, but here we treat as numeric value comparison)
            print(f"{num1} == {num2}: {'True' if num1 == num2 else 'False'}")

    except ValueError:
        raise RuntimeError("Invalid number format provided.") from None
    except TypeError:
        raise RuntimeError("Input types are invalid.") from None

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or arguments.
    # Using strings that represent valid numbers (integers and floats).
    sample_input_1 = "42"
    sample_input_2 = "42"

    try:
        compare_numbers(sample_input_1, sample_input_2)
    except RuntimeError as e:
        print(f"Error during execution: {e}")