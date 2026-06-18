def is_positive(value):
    """Check if a number is positive."""
    return value > 0

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or network access
    samples = [1, -5, 0.5, "not_a_number", True]

    for val in samples:
        try:
            if isinstance(val, (int, float)):
                result = is_positive(float(val))
                print(f"Value {val} ({type(val).__name__}): {'Positive' if result else 'Not Positive'}")
            elif isinstance(val, str):
                # Attempt to parse string as integer or float for demonstration of error handling logic
                try:
                    num = int(val)
                    result = is_positive(num)
                    print(f"String '{val}' parsed as {num}: {'Positive' if result else 'Not Positive'}")
                except ValueError:
                    # Handle non-integer/non-float string input gracefully without crashing the script
                    try:
                        num = float(val)
                        result = is_positive(num)
                        print(f"String '{val}' parsed as {num}: {'Positive' if result else 'Not Positive'}")
                    except ValueError:
                        # If it's not a valid number at all, we treat the conversion attempt as an error case for robustness
                        # However, since the task asks to handle non-integer inputs specifically in the context of integer input logic,
                        # and our main function expects integers, let's focus on strict int validation if needed.
                        # But given the instruction "takes a single integer input", we should ensure the core check handles ints strictly.
                        print(f"String '{val}' is not a valid number.")
            else:
                print(f"Unsupported type for value {val}: {type(val).__name__}")

        except Exception as e:
            # Catch any unexpected errors during processing to keep it robust
            print(f"Error occurred while checking value {val} ({type(val).__name__}): {e}")