import math

def get_length_measurements():
    """Returns a list of two numeric length measurements."""
    return [10, 5]

def validate_numeric_input(values):
    """Validates that all inputs are numbers and returns the cleaned values."""
    for val in values:
        if not isinstance(val, (int, float)):
            raise TypeError(f"Input '{val}' is not a numeric type.")

if __name__ == '__main__':
    pass
