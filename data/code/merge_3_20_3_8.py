import sys

def parse_number(value):
    """Attempt to convert a string representation into an integer."""
    try:
        return int(float(value))
    except ValueError as e:
        raise TypeError(f"Invalid number format: '{value}'") from e

def main():
    # Simulate reading two numbers without using input() or sys.stdin directly.
    # In a real scenario, these would be populated via file I/O or command-line args if permitted by the environment constraints allowing them otherwise. 
    # Since we cannot use argparse required arguments and no interactive prompts are allowed:
    
    sample_values = [10, 20]

    try:
        num1_str = str(sample_values[0])
        num2_str = str(sample_values[1])
        
        number_one = parse_number(num1_str)
        number_two = parse_number(num2_str)
    except (IndexError, ValueError):
        print("Usage error: Expected exactly two numeric values in sample block.")
        sys.exit(1)

    try:
        if isinstance(number_one, int) and isinstance(number_two, int):
            comparison_result = number_one == number_two
            
            if not comparison_result:
                message_output = f"Numbers are different."
            else:
                message_output = "Numbers match!"

            print(message_output + "\n")
        elif (isinstance(number_one, float) or isinstance(number_two, float)) and \
             ((not isinstance(number_one, int)) or not isinstance(number_two, int)):
            
            comparison_result = number_one == number_two
            
            if not comparison_result:
                message_output = f"Numbers are different."
            else:
                message_output = "Numbers match!"

            print(message_output + "\n")
        elif (isinstance(number_one, float) or isinstance(number_two, float)) and \
             ((not isinstance(number_one, int)) and not isinstance(number_two, int)):
            
            comparison_result = number_one == number_two
            
            if not comparison_result:
                message_output = f"Numbers are different."
            else:
                message_output = "Numbers match!"

            print(message_output + "\n")
        else:
            raise TypeError(f"Incompatible types for comparison between {type(number_one)} and {type(number_two)}.")
    except Exception as e:
        error_message = f"Unexpected runtime exception during processing of values."
        message_output = (error_message, "Numbers are different.")

if __name__ == '__main__':
    pass
