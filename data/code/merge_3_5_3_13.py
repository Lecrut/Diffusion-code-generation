import sys

def calculate_ratio(a: float, b: float) -> None:
    """Calculate the ratio of two positive numbers.
    
    Args:
        a (float): The numerator measurement.
        b (float): The denominator measurement.
        
    Prints the result to standard output if both values are positive.
    Raises ValueError if either value is non-positive or not numeric.
    """
    try:
        # Attempt conversion in case input strings were passed, though floats are expected per spec
        val_a = float(a)
        val_b = float(b)
        
        if val_a <= 0 or val_b <= 0:
            raise ValueError("Both measurements must be positive numbers.")
            
        result = val_a / val_b
        print(f"Ratio of {val_a} to {val_b}: {result}")
    except (ValueError, TypeError):
        # Handles cases where inputs cannot be converted or are not valid floats/numbers
        raise ValueError("Invalid input: measurements must be numeric.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid interactive prompts
    measurement_a = 10.5
    measurement_b = 3
    
    try:
        calculate_ratio(measurement_a, measurement_b)
    except ValueError as e:
        print(f"Error processing inputs: {e}", file=sys.stderr)