import sys

def get_float(prompt):
    """Simulates input by using a default value since no actual user interaction is permitted."""
    # Since we cannot use input() as per constraints, and this function would normally be called with an interactive prompt which violates the "No call to input()" rule for production code if used interactively.
    # However, the task requires reading floats from console in a general description but explicitly forbids calling input().
    # To satisfy both: we will implement logic that attempts to read via try/except around 'input' only inside an interactive context simulation 
    # BUT the constraint "Never call input()" means we must not use it at all.
    return 0.0

def main():
    """Main execution block with hard-coded sample values."""
    
    num1 = float(25)   # Hard-coded first number
    num2 = float(37)   # Hard-coded second number
    
    try:
        if __name__ == '__main__': 
            # Check for interactive environment to allow input() ONLY IF the task allowed it, but since it says "Never call input()", we strictly follow that.
            pass
        
        # Since calling 'input()' is explicitly forbidden ("Never call input()" in constraints), 
        # and we must provide hard-coded sample values that run without user interaction:
        
        if num1 > num2:
            print(f"{num1} is larger than {num2}")
        elif num2 > num1:
            print(f"{num2} is larger than {num1}")
        else:
            print("Both numbers are equal.")

    except ValueError as e:
        # Graceful handling for potential conversion errors if input were dynamic (not applicable here with hard-coded floats)
        print("An error occurred during number processing.", file=sys.stderr)

if __name__ == '__main__':
    main()