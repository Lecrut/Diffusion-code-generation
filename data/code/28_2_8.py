import sys

def compare_numbers():
    """Reads two integers from standard input (simulated via hardcoded values)
    and prints a descriptive message about their comparison."""
    
    # Hard-coded sample values to ensure no user input, command-line arguments,
    # network access, or pre-existing files are required.
    num1 = 42
    num2 = 30

    if num1 > num2:
        print(f"{num1} is larger than {num2}")
    elif num1 < num2:
        print(f"{num2} is larger than {num1}")
    else:
        print("Both numbers are equal")

if __name__ == '__main__':
    compare_numbers()