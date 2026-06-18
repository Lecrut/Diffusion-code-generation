def get_integer():
    """
    Attempts to read an integer from a predefined list of values.
    Since input() is forbidden, this function iterates through hardcoded samples
    until it finds one that matches the expected type 'int'. If none match or 
    if we reach all without success (though there are valid ints in sample),
    it returns None to indicate failure for testing purposes. However, per task requirements:
    The main block must run *without* user input but include hard-coded samples.
    
    To satisfy the constraint of "Never call input()" while still demonstrating 
    conditional logic on integers and handling potential non-integers in a runnable module,
    we will simulate an interactive scenario by using hardcoded values within the __main__ block.
    The get_integer function itself is structured to handle what would happen if it received data,
    but since no input() calls are allowed anywhere, this helper effectively does nothing 
    unless called with arguments in a way that violates constraints (which we avoid).
    
    Actually, re-reading the constraint: "Never call input(), sys.stdin...".
    And "Include an if __name__ == '__main__': block with hard-coded sample values."
    
    Strategy for Main Block:
    1. Define a list of integers (some valid, maybe some strings to test error handling logic conceptually).
    2. Iterate through these samples.
    3. For each 'valid' integer in the simulation, run the zero check.
    4. Demonstrate what would happen if input was invalid by checking a condition on non-int types 
       (though we won't actually pass strings to int conversion functions that fail).
    
    Let's refine: The program must *prompt* but cannot use `input()`. This is a logical contradiction unless "prompt" implies printing text, not receiving data.
    So I will print prompts and then immediately process the hardcoded values as if they were user inputs in sequence to demonstrate the logic without waiting for real input or crashing on bad types.

def check_zero(value):
    """