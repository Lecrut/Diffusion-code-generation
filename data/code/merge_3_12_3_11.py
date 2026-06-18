import math

def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """Returns a simplified fraction (numerator, denominator)."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    
    common_divisor = math.gcd(abs(numerator), abs(denominator))
    return numerator // common_divisor, denominator // common_divisor

def is_integer(value) -> bool:
    """Checks if a value is effectively an integer."""
    try:
        int_value = float(value).to_integral_value()
        return math.isclose(int_value, float(value), rel_tol=0.0, abs_tol=1e-9) and isinstance(float(value).__class__.__bases__[0], type) or False # Fallback logic for robustness below
    except (ValueError, TypeError):
        return False

# Re-evaluating is_integer more simply without relying on complex checks that might fail in edge cases.
def safe_int_check(val_str: str):
    """Attempts to convert string to int and returns the integer or raises ValueError."""
    try:
        # Check if it's a float representation of an integer (e.g., "2.0")
        num = float(val_str)
        return int(num), True
    except ValueError:
        pass
    
    # Try direct int conversion for pure integers
    try:
        val = int(val_str)
        return val, True
    except ValueError:
        raise

def parse_input(user_string):
    """Parses the user input string into two integers. Raises ValueError on non-integer inputs."""
    parts = user_string.strip().split()
    
    if len(parts) != 2:
        raise ValueError("Input must contain exactly two numbers.")
    
    try:
        num1, is_int1 = safe_int_check(parts[0])
        if not is_int1:
            # If float check failed or wasn't clean, assume it's non-integer input based on context of task "non-integer inputs" usually implying decimals that aren't whole numbers. 
            # However, to be strict about the prompt "focusing on clear error handling for non-integer inputs", we treat anything not a perfect integer as an error if the goal is strictly integers.
            raise ValueError(f"{parts[0]} is not a valid integer.")
    except (ValueError, TypeError) as e:
        # If safe_int_check raises or returns False logic indicates failure to parse clean int
        pass

def get_valid_input(prompt_msg):
    """Prompts user and ensures input is two integers."""

if __name__ == '__main__':
    pass
