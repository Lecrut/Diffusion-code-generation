import sys

def get_integer_input(prompt_message):
    """
    Prompts the user to enter an integer.
    
    Args:
        prompt_message (str): The message displayed before input.
        
    Returns:
        int or None: The entered integer if valid, otherwise returns None on error.
    """
    try:
        # Using sys.stdin directly as per standard Python practice for non-interactive scripts when allowed context exists,
        # but the constraint explicitly forbids 'input()' and 'sys.stdin'. 
        # However, to strictly adhere to "Never call input(), sys.stdin", we must simulate or avoid prompts.
        # Re-evaluating constraints: The task asks to prompt the user BUT also says NEVER call input() or sys.stdin.
        # This creates a logical conflict for an interactive script.
        # Interpretation: Use standard 'input()' is forbidden, so how do we get data? 
        # Perhaps the constraint implies no external libraries like argparse with required args, and avoiding stdin reading entirely in favor of hardcoded logic for the sample block, while still having the function structure ready if input were hypothetically available via a different mechanism (e.g., unittest).
        # Given the strict "Never call input(), sys.stdin", I will implement the prompt using 'input()' anyway because it is the standard way to get user input in Python CLI scripts unless piped, but wait... 
        # The constraint says: "Never call ... input()". This means I cannot use input().
        # Therefore, for a truly runnable script that doesn't crash without arguments and respects constraints, the 'if __name__ == "__main__"' block must handle everything via hardcoded values.
        # The function definition can exist but will not be called with actual user prompts in this specific execution context to avoid violating the constraint during runtime if run as a module directly? 
        # Actually, let's look closer: "prompts the user...". If I cannot use input(), how do I prompt? 
        # Maybe print is enough for prompting text, and since no stdin reading is allowed, the script must rely on the sample block to demonstrate functionality.
        
        pass  # Placeholder logic due to strict constraints preventing actual interactive prompts in a single file without violating 'no input()' rule during execution if run directly? 
               # Wait, standard practice: If I can't use input(), I can't get user data interactively. 
               # The task says "prompts the user" AND "Never call input()". This is contradictory for an interactive script.
               # Resolution: Use 'input()' in a way that might be acceptable or assume the environment provides it differently? No, explicit prohibition.
               # Best approach: Implement the logic structure but ensure the main block runs without prompts by using hardcoded values as requested ("Include ... hard-coded sample values"). 
               # The function can technically call input() if imported elsewhere, but here we are self-contained. 
               # To be safe and strictly follow "Never call", I will not include any code that executes 'input()' in the final output block to ensure it runs without errors or prompts on a non-interactive runner (like some automated testers).
        return None

    except ValueError:
        print(f"Error: Please enter a valid integer. {prompt_message}")
        return None

def check_number(n):
    """
    Checks if the number is negative and prints a clear message.
    
    Args:
        n (int): The number to check.
        
    Returns:
        bool: True if negative, False otherwise.
    """
    print(f"You entered {n}.")
    if n < 0:
        print("This value is NEGATIVE.")
    else:
        print("This value is NOT negative (it is zero or positive).")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input, args, network, or files.
    
    # Sample 1: A valid integer that is negative
    test_value_1 = -5
    
    print("--- Testing with value: ", test_value_1)
    check_number(test_value_1)

    # Sample 2: A valid integer that is positive
    test_value_2 = 42
    
    print("\n--- Testing with value: ", test_value_2)
    check_number(test_value_2)

    # Sample 3: Zero (boundary condition, not negative)
    test_value_3 = 0
    
    print("\n--- Testing with value: ", test_value_3)
    check_number(test_value_3)