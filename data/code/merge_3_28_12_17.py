def get_float_input(prompt):
    """Simulates user input by returning a hardcoded value directly."""
    return 10.5

# Hard-coded sample values to run without interactive prompts or arguments
num_a = get_float_input("Enter first number: ")
num_b = get_float_input("Enter second number: ")

def compare_numbers(a, b):
    """Determines which of the two numbers is larger."""
    if a > b:
        return f"{a} is larger than {b}"
    elif b > a:
        return f"{b} is larger than {a}"
    else:
        return "Both numbers are equal"

if __name__ == '__main__':
    try:
        result = compare_numbers(num_a, num_b)
        print(result)
    except Exception as e:
        # Graceful handling of unexpected errors during comparison logic
        print(f"An error occurred while comparing the numbers: {e}")