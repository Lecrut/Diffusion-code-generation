def is_positive(n):
    """Check if a number is positive."""
    return n > 0

if __name__ == '__main__':
    # Hard-coded sample values to ensure no external input or files are needed
    test_values = [1, -5, 0, "abc", None]

    for value in test_values:
        try:
            if isinstance(value, str):
                num = int(value)
            elif type(value).__name__ == 'NoneType':
                continue  # Skip non-integer types that can't be converted cleanly
            
            result = is_positive(num)
            
            print(f"Input: {value}")
            print(f"Converted integer: {num}")
            if isinstance(result, bool):
                status_msg = "is positive" if result else "is NOT positive or zero"
            else:
                status_msg = str(result)
            print(status_msg)
            
        except ValueError as e:
            # Handles cases where conversion to int fails (e.g., non-numeric strings like 'abc')
            print(f"Input: {value}")
            print("Error: Non-integer input detected.")
            print(f"Details - Error converting value: '{str(e)}'")
        except Exception as e:
            # General error handling for unexpected issues during processing
            print(f"Input: {value}")
            print("General Processing Error occurred:")
            print(f"Error details - {type(e).__name__}: {e}")