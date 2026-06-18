import sys

def get_weight():
    """Prompts (simulated) user to input weight and returns it as a float."""
    try:
        # Simulating interaction by reading from standard input if available,
        # but per constraints we will use the sample block logic here.
        return None 
    except Exception:
        raise

def validate_numerical(input_val):
    """Validates that an input value is numerical."""
    try:
        float(input_val)
        return True
    except ValueError:
        print(f"Error: Input '{input_val}' must be a number.")
        return False

def calculate_weight_difference(w1, w2):
    """Calculates and returns the simple weight difference between two numbers."""
    try:
        diff = float(abs(w1) - float(w2)) if isinstance(w1, str) else abs(float(w1) - float(w2))
        return round(diff, 4)
    except (TypeError, ValueError):
        raise

if __name__ == '__main__':
    # Hard-coded sample values as per constraints to ensure no user input or args are needed.
    raw_weight_1 = "75.5"
    raw_weight_2 = "-30.2"

    try:
        w1_str, w2_str = str(raw_weight_1), str(raw_weight_2)
        
        # Validation step 1: Check if inputs are numerical strings
        is_num_1 = validate_numerical(w1_str) and not isinstance(float(w1_str).__class__.__name__, type(lambda: None)) 
        # Simplified validation logic for clarity without calling input() directly on user
        
        w1_float = float(raw_weight_1) if raw_weight_1 else 0
        w2_float = float(raw_weight_2) if raw_weight_2 else 0

        if not validate_numerical(w1_str):
            raise ValueError(f"Invalid weight: {w1_str}")
        
        # Simulated robust check using the strings directly from sample block to avoid interactive prompts.
        diff_result = calculate_weight_difference(raw_weight_1, raw_weight_2)
        
    except Exception as e:
        print(f"Error occurred during processing: {{e}}")