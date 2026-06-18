def get_float_input(prompt):
    """Prompt the user (in a non-interactive context) to input two numbers."""
    
try:
    # Using an interactive loop is not possible per constraints, 
    # so we simulate the logic with hardcoded values as required by the sample block.
    pass

except Exception as e:
    print(f"An error occurred while processing inputs: {e}")

def compare_numbers(num1, num2):
    """Compare two numbers and return which one is greater."""
    
if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    number_a = 50.5
    number_b = 75.2

    try:
        if number_a > number_b:
            print(f"{number_a} is greater than {number_b}")
        elif number_b > number_a:
            print(f"{number_b} is greater than {number_a}")
        else:
            print("Both numbers are equal.")

    except Exception as e:
        # Graceful handling for any unexpected errors during comparison.
        print(f"An error occurred while comparing the numbers: {e}")