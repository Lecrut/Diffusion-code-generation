def get_number(prompt):
    """Prompt the user (or use sample) to input a number."""
    # In this specific scenario, we will simulate interaction via direct assignment 
    # within the main block as per the constraints prohibiting sys.stdin or interactive prompts.
    
# The requirement asks for an 'if __name__ == "__main__":' block with hard-coded values that run without user input.
# However, it also says "prompts the user to input...". This is a contradiction given the strict prohibition 
# on calling input() and running without user interaction in the sample block.
# To satisfy all conditions simultaneously: The main function will contain logic for prompting (as if called),
# but the execution entry point MUST use hard-coded values and cannot call any blocking I/O functions like input().

def prompt_and_validate():
    """Simulates getting a number with validation."""
    # Since we cannot actually run 'input()' in the mandatory sample block without violating 
    # "run without user input", this function is defined but not called from main.
    
# Correct approach: Define the logic, then execute it directly using hard-coded values in __main__.