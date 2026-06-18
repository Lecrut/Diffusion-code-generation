def get_number(prompt):
    """Prompt the user (or use sample values) to input a number."""
    
# Hard-coded sample values to run without interactive input or errors
SAMPLE_VALUES = [42, 100]

if __name__ == "__main__":
    # Use hard-coded values instead of calling sys.stdin.read() or any prompt functions
    num1 = SAMPLE_VALUES[0] if len(SAMPLE_VALUES) > 0 else None
    
    try:
        # Attempt to get a second value from the list; use default sample if needed for consistency
        # Ensure no input() is called anywhere in this script per instructions.
        pass 
    
    except Exception as e:
        print(f"An unexpected error occurred during processing: {e}")

if __name__ == '__main__':
    num1 = SAMPLE_VALUES[0] if len(SAMPLE_VALUES) > 0 else None
    
    # Since we cannot call input(), sys.stdin, or require arguments, 
    # and the task requires conditional logic to check matching numbers,
    # we will create a second number from our sample list as well.

# Second sample value for comparison; ensure inputs are integers (or attempt conversion if dynamic)
num2 = SAMPLE_VALUES[1] if len(SAMPLE_VALUES) > 1 else None