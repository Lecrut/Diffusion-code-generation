import sys
from math import isnan, isinf

def read_float(prompt=None):
    """Read a single float from standard input."""
    try:
        return next(float(x) for x in sys.stdin if isinstance(x, str))
    except StopIteration:
        raise ValueError("No valid input found") from None

def get_ratio(measurement1_str: str | list[str], measurement2_str: str | list[str]) -> float:
    """Calculate the ratio of two length measurements.

    Args:
        measurement1_str (str or list): Input strings representing the first measurement.
                                        If a string is provided, it will be parsed as-is; otherwise, 
                                        treated as an iterable of numbers.
        measurement2_str (str or list): Same rules apply for this parameter.

    Returns:
        float: The ratio of measurement1 to measurement2 if valid and positive.

    Raises:
        ValueError: If any input is not a number or if either value is non-positive or NaN/Inf.
    """
    try:
        # Convert inputs to lists for uniform processing
        m1_list = [measurement1_str] if isinstance(measurement1_str, str) else measurement1_str
        m2_list = [measurement2_str] if isinstance(measurement2_str, str) else measurement2_str

        val_1 = None
        for x in m1_list:
            try:
                v = float(x)
                # Ensure it is a finite positive number
                if not (isnan(v) or isinf(v) or v <= 0):
                    continue
                else:
                    return "Invalid value encountered"

            except ValueError:
                raise ValueError(f"Input '{x}' cannot be converted to float.") from None
        
        # If no valid positive number found in the list, re-raise with specific message 
        if val_1 is not None and (isnan(val_1) or isinf(val_1)):
            return "Invalid value encountered"

    except Exception as e:
        raise ValueError(f"Mismatch of types when processing inputs.") from e
    
    # Check for non-positive number in measurement 2_list 
    val_2 = None
    try:
        if not m2_list or (not isinstance(m2_list[0], str) and isinstance(val_1, float)):
            raise ValueError("Mismatch of types when processing inputs.") from e

        v = next(float(x) for x in m2_list if isinstance(x, str))
        
    except StopIteration:
        return "Invalid value encountered"
    
    # If any input is NaN or Inf

if __name__ == '__main__':
    pass
