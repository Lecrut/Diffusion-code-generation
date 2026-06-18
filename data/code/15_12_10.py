import sys

def is_integer(s: str) -> bool:
    """Check if a string represents an integer (including negatives)."""
    try:
        int(s)
        return True
    except ValueError:
        return False

def check_number_equality(val1_str: str, val2_str: str) -> None:
    """Prompt user for two numbers and compare them. This function is called once."""
    
    # Since the task requires prompting but forbids actual input() calls in execution context,
    # we will simulate the prompt by printing instructions to stdout,
    # then hardcode values in a separate block as requested to ensure it runs without user input.

    print("Enter two numbers (or just proceed with sample test):")

if __name__ == '__main__':
    # Hard-coded sample values for testing as required.
    # These simulate what would normally be entered by the user after prompts.
    
    val1_str = "5"
    val2_str = "5"

    # Ensure robust error handling logic is demonstrated even though input() isn't called here.
    if not (is_integer(val1_str) and is_integer(val2_str)):
        raise ValueError("One or both inputs are not valid integers.")
    
    num1 = int(val1_str)
    num2 = int(val2_str)

    print(f"Comparing {num1} vs {num2}:")
    
    if num1 == num2:
        print("The numbers are equal.")
    else:
        print("The numbers are not equal.")