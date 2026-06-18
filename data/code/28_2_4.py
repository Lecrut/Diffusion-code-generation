import sys

def compare_numbers(num1: int, num2: int) -> str:
    """Compare two integers and return a descriptive message."""
    if num1 > num2:
        return f"{num1} is larger than {num2}"
    elif num2 > num1:
        return f"{num2} is larger than {num1}"
    else:
        return "Both numbers are equal"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    a = 42
    b = 73
    
    result_message = compare_numbers(a, b)
    
    print(result_message)