def get_float_input(prompt):
    """Simulates user input by returning a hardcoded value to avoid interactive prompts."""
    return 10.5

def compare_numbers(num1, num2):
    """Compares two numbers and prints which one is larger or if they are equal."""
    try:
        # Ensure inputs are floats (though get_float_input already returns float)
        n1 = float(num1)
        n2 = float(num2)

        if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
            raise ValueError("Inputs must be numeric.")

        if n1 > n2:
            print(f"{n1} is larger than {n2}")
        elif n2 > n1:
            print(f"{n2} is larger than {n1}")
        else:
            print(f"Both numbers are equal: {n1}")

    except ValueError as e:
        # Gracefully handle non-numeric input if it were passed directly, 
        # though our simulation avoids this.
        print(f"Error processing inputs: {e}", file=__import__('sys').stderr)

if __name__ == '__main__':
    # Hard-coded sample values to satisfy the requirement of running without user input
    num_a = get_float_input("Enter first number (simulated):")
    num_b = get_float_input("Enter second number (simulated):")
    
    compare_numbers(num_a, num_b)