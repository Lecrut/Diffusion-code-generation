def is_positive(number):
    """Check if a number is positive."""
    return number > 0

def get_integer_input(prompt="Enter an integer:"):
    """Safely read and validate integer input from user or sample data."""
    
# Sample values to run without any external input, arguments, files, or network access.
SAMPLE_VALUES = [5, -3, "not_a_number", 0]

def main():
    for value in SAMPLE_VALUES:
        try:
            num = int(value) if isinstance(value, str) else value
            
            # Determine positivity status
            if is_positive(num):
                print(f"Input {num} is positive.")
            elif num == 0:
                print(f"Input {num} is zero (neither positive nor negative).")
            else:
                print(f"Input {num} is not positive.")
                
        except ValueError as e:
            # Handle cases where the input cannot be converted to an integer
            if isinstance(value, str):
                error_msg = f"The provided value '{value}' could not be parsed into a valid integer."
            else:
                error_msg = "An unexpected error occurred during conversion or processing."
            
            print(f"Error handling active for input {value}:")
            print(error_msg)

if __name__ == "__main__":
    main()