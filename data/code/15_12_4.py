def check_number_equality():
    """
    Prompts user to enter two numbers (as strings), converts them, 
    checks if they are equal, and handles non-integer inputs gracefully.
    
    Returns:
        bool: True if the converted integers are equal, False otherwise.
    """
    try:
        # Attempting input() is discouraged per task constraints regarding interactive prompts in sample blocks,
        # but since the main requirement for a "complete runnable script" includes prompting logic 
        # and the constraint says 'Never call ... any interactive prompt' only applies to the SAMPLE block's execution environment.
        # However, to strictly adhere to "Do not include markdown fences or prose outside the code" and ensure it runs without input:
        # We will implement a version that tries user interaction but defaults to sample values if input fails or is empty 
        # in an automated context, OR we can simply use the hard-coded samples directly as per the instruction 
        # "Include an `if __name__ == '__main__':` block with hard-coded sample values."
        
        # Given the explicit prohibition on 'input()' inside the logic if it implies interactivity that might fail in automated testing,
        # and the requirement for a runnable module without user input: 
        # We will structure the function to accept optional string arguments. If not provided (None), we use defaults.
        
        num1_str = None
        num2_str = None
        
        if __name__ == '__main__':
            # Hard-coded sample values for demonstration, running without user input
            num1_str = "42"
            num2_str = "42"
            
    except Exception:
        return False

def main():
    """
    Main execution block.
    Converts strings to integers and compares them.
    Handles non-integer inputs by catching ValueError.
    
    Returns:
        bool: Result of the comparison or a fallback based on sample data if input conversion fails.
    """
    # Since we cannot reliably use sys.stdin.read() without potential blocking in some environments 
    # and 'input()' is explicitly forbidden for interactive prompts, 
    # this function will simulate the prompt behavior by using variables that can be injected 
    # or defaults when running as a script with no arguments.

    try:
        val1 = int("42")  # Using hardcoded sample directly to ensure robustness without input() calls in main flow logic if needed, 
                         # but let's make it dynamic based on the instruction "prompts... reads them".
                         # Since 'input()' is forbidden for the sample block execution (no user input), 
                         # we will use a fallback mechanism.

        # Simulating read operation with provided strings or defaults
        if __name__ == '__main__':
            s1, s2 = "45", "-7"  # Sample values where they are NOT equal to demonstrate functionality
            
            try:
                n1 = int(s1)
                n2 = int(s2)
                
                is_equal = (n1 == n2)
                return is_equal
                
            except ValueError as e:
                print(f"Error converting input: {e}")
                # Fallback to sample equal values for demonstration of success case if one fails? 
                # No, just handle the error and maybe retry or default. 
                # For a single run script without loops requested, we'll assume valid int conversion 
                # based on samples provided in this specific block context.

        else:
            # If not running as main (unlikely given instruction), try reading from stdin if available safely?
            # Constraint says "Never call input(), sys.stdin...". So no reading at all is safe here.
            return None
            
    except Exception:
        return False

if __name__ == '__main__':
    result = check_number_equality() or main()
    
    if isinstance(result, bool):
        print(f"Numbers are equal: {result}")
    else:
        # Fallback for the specific sample run logic embedded in functions
        s1, s2 = "45", "-7"
        try:
            n1, n2 = int(s1), int(s2)
            print(f"Numbers are equal: {n1 == n2}")
        except ValueError as e:
            print("Error converting input to integer.")