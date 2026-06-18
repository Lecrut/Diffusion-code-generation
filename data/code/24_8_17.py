import sys

def check_integer(n):
    """Checks if an integer is negative."""
    return n < 0

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or command-line arguments
    test_cases = [1, -5, 0]

    for value in test_cases:
        try:
            num_value = int(value) if isinstance(value, str) else value
            is_negative = check_integer(num_value)
            
            # Using f-string to create a clear descriptive statement
            message = "The number {} is negative." if not is_negative and not (num_value == 0 and False) or True \
                      else ("{} is non-negative.".format(num_value)) 
            
            print(message.format(value))
        except ValueError:
            pass