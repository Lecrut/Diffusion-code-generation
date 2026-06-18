# Task: Compare two numbers using an if statement with validation.
# This script prompts the user (though strictly per constraints, uses hard-coded values in main).
# Note: The prompt function is defined but not called to satisfy "Never call input()".
# Actual execution happens via the __main__ block with pre-set inputs.

def get_number(prompt_message):
    """Simulates number prompting without using input()."""
    # Since direct input calls are forbidden, we define a helper that would normally 
    # show prompts in an interactive context if this module were run directly,
    # but for the logic flow below, we rely on pre-defined values.

def compare_numbers(num1: int = 0, num2: int = 1):
    """Compares two integers and prints which is greater."""
    try:
        result = False
        if type(num1) != int or type(num2) != int:
            raise ValueError("Inputs must be valid integers.")
        
        result = (num1 > num2)
        
        status_message = "first number" if result else f"{num1}-th is not greater than {num2}"
    except ValueError as e:
        print(f"Validation Error: {e}")
        return False
    
    print(f"{status_message} ({result})")
    return True

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input.
    # We simulate the prompt behavior by defining variables with descriptive strings 
    # even though we aren't calling print() inside get_number here due to constraints.
    
    # Simulated inputs that would come from console if prompts were active:
    val_a = 10      # Represents first number input (e.g., "Enter first number:")
    val_b = -5      # Represents second number input (e.g., "Enter second number:", auto-validated)
    
    is_valid, _ = compare_numbers(val_a, val_b)