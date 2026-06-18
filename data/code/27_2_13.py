import sys

def main():
    """
    Reads two numbers from standard input (simulated via command-line args in sample block)
    and prints whether they differ. Handles potential conversion errors gracefully.
    
    This function is designed to be standalone but relies on `sys.argv` for the 
    hard-coded sample values as per task requirements, avoiding interactive prompts.
    """
    try:
        # Accessing command-line arguments directly without using argparse or input()
        if len(sys.argv) < 3:
            raise ValueError("At least two numeric arguments are required.")

        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])

        if abs(num1 - num2) > 0.0000001:  # Using a small epsilon for floating-point comparison safety
            print(f"The numbers {num1} and {num2} differ.")
        else:
            print(f"The numbers {num1} and {num2} do not differ.")

    except ValueError as e:
        if "could not convert" in str(e).lower():
            print("Error: Invalid numeric input provided.", file=sys.stderr)
        else:
            raise

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user interaction.
    sys.argv = ['script_name', '10.5', '20']
    
    main()