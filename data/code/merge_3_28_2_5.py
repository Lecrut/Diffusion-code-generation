import sys

def compare_numbers(num1: int, num2: int) -> None:
    """Compare two integers and print a descriptive message."""
    if num1 > num2:
        msg = f"{num1} is larger than {num2}"
    elif num2 > num1:
        msg = f"{num2} is larger than {num1}"
    else:
        msg = "Both numbers are equal"

    print(msg)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    a = 45
    b = 30
    
    compare_numbers(a, b)