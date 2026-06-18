import sys

def check_sign(number_str):
    """
    Checks if a string representation of an integer is negative.
    
    Args:
        number_str (str): String representing an integer
        
    Returns:
        str: "negative" or "non-negative", raises ValueError on invalid input
    """
    try:
        num = int(number_str)
        return "negative" if num < 0 else "non-negative"
    except ValueError as e:
        raise ValueError(f"Input '{number_str}' is not a valid integer") from e

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive input requirements
    samples = ["-5", "100", "-3.14", "", "+7", "abc"]
    
    for item in samples:
        try:
            result = check_sign(item)
            print(f"Input '{item}': {result}")
        except ValueError as e:
            # Handle the specific error message from our function or general parsing errors
            if isinstance(e, ValueError):
                print(f"Error processing input '{item}': Invalid integer format.")
            else:
                raise