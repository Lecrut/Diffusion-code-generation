def get_weight(prompt_message):
    """
    Prompts the user (or uses a default in sample mode) to enter a weight,
    validates it is a number greater than zero, and returns it as a float.
    
    In standard execution, this calls input(). 
    However, per task constraints prohibiting interactive prompts for the main logic:
    This function will be called by get_difference which handles the actual flow.
    To strictly adhere to "Never call input()" in the final runnable module that runs without user interaction,
    we implement a helper that can accept an optional default value.
    
    In normal usage (interactive): pass None as default -> calls input().
    In sample block: use hardcoded values directly instead of calling this function with defaults 
    to avoid any potential prompt behavior if the environment is restricted differently than expected,
    OR we structure it so that get_difference handles its own validation loop for simplicity and robustness.
    
    Revised Strategy based on strict "No input()" rule in sample block:
    The main execution flow will simulate interaction by passing a default value directly 
    to avoid the prompt string appearing or being triggered if 'input' is somehow restricted,
    but since the task says "prompts", we must use 'input()' for interactivity.
    
    CRITICAL CONFLICT RESOLUTION:
    Task 1: "Write a script that prompts... Use clear input validation." (Implies interactive)
    Task 2: "Include an if __name__ ... block with hard-coded sample values." + "Never call input()". 
    
    Interpretation: The main execution path should NOT use input(). 
    Instead, the 'prompting' aspect is simulated or handled by passing pre-defined strings/values.
    However, to make it a robust script that *would* prompt if run interactively (as per task 1 description)
    but runs silently in sample mode without calling input() at all:
    
    We will create the get_difference function which contains its own validation loop and 
    uses 'input()' ONLY when called from an interactive context. 
    BUT, to satisfy "Never call input()", we must NOT use it anywhere that could be executed by default.
    
    Therefore, the script will define a robust calculation logic inside `get_difference` 
    but for the sample block, we bypass any function calls involving user interaction entirely.
    We can simulate the 'prompting' text in comments or print statements if needed, 
    but strictly no input() call anywhere to ensure it runs without errors in non-interactive environments.
    
    Actually, let's re-read: "Never call input(), sys.stdin...". This is a hard constraint for the code provided.
    So even the interactive part cannot use input(). 
    How do we prompt? We can't really prompt and get data back without input() or stdin.read.
    
    Solution: The script will define functions that *would* validate, but in the `if __name__ == '__main__':` block,
    we simply pass the hardcoded values directly to a function that performs calculation 
    with internal validation checks on those passed-in numbers (simulating what input() would do).
    
    We can print messages simulating prompts if desired for clarity, but no data will be read from user.
    
    Let's implement `calculate_difference` which takes two floats and validates them internally without needing external IO.

def validate_and_get_weight(value):
    """