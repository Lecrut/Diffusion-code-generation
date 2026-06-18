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
    # Hard-coded sample values as per requirements (no user input or args)
    val_a = 42
    val_b = 73
    
    result_message = compare_numbers(val_a, val_b)
    
    print(result_message)