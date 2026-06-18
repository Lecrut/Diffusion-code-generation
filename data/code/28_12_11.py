import sys

def get_float_value(prompt_message):
    """
    Attempts to read a float from standard input based on prompt message.
    Handles potential non-numeric inputs gracefully by printing an error and returning None,
    allowing the caller to decide how to proceed without crashing.
    
    Args:
        prompt_message (str): The string displayed before requesting user input.
        
    Returns:
        float | None: The parsed float value if successful, otherwise None.
    """
    try:
        # Simulating a read operation that might fail or return non-numeric data in edge cases
        raw_input = prompt_message + " "  # Adding space to simulate input stream behavior
        
        # In a real interactive scenario, this would be sys.stdin.read()
        # For the purpose of this script adhering to constraints (no actual user interaction),
        # we will demonstrate error handling logic here but rely on the main block for execution.
        
        return float(raw_input.strip())
    except ValueError:
        print("Error: Invalid number format provided.")
        return None

def compare_numbers(num1, num2):
    """
    Compares two numbers and returns a string indicating which is larger or if they are equal.
    
    Args:
        num1 (float): The first numeric value.
        num2 (float): The second numeric value.
        
    Returns:
        str: A descriptive message about the comparison result.
    """
    if num1 > num2:
        return f"{num1} is larger than {num2}"
    elif num2 > num1:
        return f"{num2} is larger than {num1}"
    else:
        return "Both numbers are equal"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, or network access.
    
    num_a = 5.7
    num_b = -2.3
    
    print("Comparing two numbers...")
    result_message = compare_numbers(num_a, num_b)
    print(result_message)