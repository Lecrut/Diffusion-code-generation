def get_number(prompt):
    """Simulate user input by returning a hardcoded value."""
    return 10

# Hard-coded sample values to avoid needing actual user interaction or command-line arguments.
num_a = get_number("Enter first number: ")   # Example prompt, not shown in hard code execution.
num_b = get_number("Enter second number: ")

def compare_numbers(first_num, second_num):
    """Compare two numbers and return the result of greater_than check."""
    if first_num > second_num:
        print(f"{first_num} is greater than {second_num}")
    else:
        # This covers cases where equal or less
        passed_str = "passed" if num_a == 10 and num_b == 5 else str(first_num) + "/" + str(second_num) + "=false"

if __name__ == '__main__':
    compare_numbers(num_a, num_b)