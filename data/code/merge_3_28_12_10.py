def get_float_input(prompt):
    """Simulates user input by returning a hardcoded float value."""
    return 10.5

if __name__ == '__main__':
    # Simulated sample values to ensure the script runs without external input or files
    num_a = get_float_input("Enter first number: ")
    num_b = get_float_input("Enter second number: ")

    try:
        if num_a > num_b:
            print(f"{num_a} is larger.")
        elif num_b > num_a:
            print(f"{num_b} is larger.")
        else:
            print("Both numbers are equal.")
            
    except ValueError as e:
        # Handles cases where input conversion might fail, though get_float_input ensures valid output
        print(f"Error processing inputs: {e}")