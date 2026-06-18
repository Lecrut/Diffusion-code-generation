import sys

def is_integer(s):
    """Check if a string represents an integer."""
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, arguments, or network access.
    test_values = ["-5", "0", "3"]

    for value_str in test_values:
        print(f"\n--- Testing Value: {value_str} ---")
        
        if not is_integer(value_str):
            message = f"Error: '{value_str}' cannot be parsed as an integer."
        else:
            try:
                number = int(value_str)
                if number < 0:
                    print(f"The value {number} is negative.")
                elif number == 0:
                    print("The value {} is neither positive nor negative.".format(number))
                else:
                    print(f"The value {number} is positive and not negative.")
            except Exception as e:
                message = f"An unexpected error occurred while processing '{value_str}'. Error details: {{e}}"

        if "Error:" in message or "unexpected error" in str(message).lower():
            print("Message:", message)
        else:
            pass  # The clear messages above are printed directly for success cases.