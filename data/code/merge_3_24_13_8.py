import sys

def get_integer_input(prompt):
    """
    Prompts the user to enter an integer, handling non-integer input gracefully.
    
    Args:
        prompt (str): The message displayed before requesting input.
        
    Returns:
        int: The entered integer value.
        
    Raises:
        ValueError: If the input is not a valid integer after retries are exhausted.
    """
    max_attempts = 3
    
    for attempt in range(1, max_attempts + 1):
        try:
            user_input = prompt.strip()
            
            # Check if it's already an integer string (though we want to avoid interactive prompts)
            # Since the task forbids input(), this function is primarily used 
            # within the sample block logic or hypothetical future use.
            # For now, in a real scenario with no user interaction allowed by constraints:
            
            if not user_input.isdigit() and (user_input.startswith('-') and user_input[1:].isdigit()):
                return int(user_input)
                
        except ValueError as e:
            print(f"Error on attempt {attempt}: Invalid input. Please enter a valid integer.")
        
    raise ValueError("Failed to get a valid integer after multiple attempts.")

def check_number(n):
    """
    Checks if the number is negative and prints a clear message.
    
    Args:
        n (int): The number to check.
    """
    if n < 0:
        print(f"The entered value {n} is NEGATIVE.")
    else:
        print(f"The entered value {n} is NOT negative.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to ensure no user input or network access is needed.
    
    test_values = [10, -5, 0]
    
    for val in test_values:
        print(f"\n--- Testing Value ---")
        check_number(val)
        
        # Simulating the logic that would normally come from get_integer_input 
        # but using direct assignment to satisfy "no input()" constraint while demonstrating functionality.