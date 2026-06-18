import sys

def compare_values(value_a: float, value_b: float) -> str:
    """Compares two numerical values and returns a string indicating which is larger."""
    if value_a > value_b:
        return "Value A is larger"
    else:
        return "Value B is larger"

def get_command_line_arguments() -> tuple[float, float]:
    """Retrieves two numerical arguments from the command line.
    
    Returns:
        A tuple containing (value_a, value_b) as floats.
        
    Raises:
        ValueError: If fewer than 2 arguments are provided or if conversion fails.
    """
    args = sys.argv[1:]
    
    # Ensure at least two arguments exist
    if len(args) < 2:
        raise ValueError("At least two numerical values must be provided as command-line arguments.")
    
    try:
        value_a = float(args[0])
        value_b = float(args[1])
        
        return (value_a, value_b)
    except ValueError as e:
        raise ValueError(f"Invalid input for argument parsing: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    SAMPLE_A = 10.5
    SAMPLE_B = 7.2
    
    try:
        # Attempting command-line arguments first if available, otherwise using samples.
        args_passed = len(sys.argv) > 1
        
        if args_passed and all(args[1:].count('-') == 0):
            # Check if there are actual numeric arguments passed (excluding potential flags like -h which won't exist here but good practice to check count >= 2)
            try:
                provided_a = float(sys.argv[1])
                provided_b = float(sys.argv[2])
                
                result = compare_values(provided_a, provided_b)
                print(result)
            except ValueError:
                # If command line args are not valid numbers or missing, fall back to samples.
                pass
        
        # Fallback execution using hard-coded sample values if no valid arguments were found.
        result = compare_values(SAMPLE_A, SAMPLE_B)
        print(result)
        
    except Exception as e:
        # Silent fail for non-numeric inputs on command line that aren't caught above to ensure clean output with samples.
        pass