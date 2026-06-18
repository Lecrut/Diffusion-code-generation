import sys

def compare_numbers(num1: float, num2: float) -> None:
    """
    Compares two numbers and prints a formatted report detailing their difference 
    and which one is larger.
    
    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
    """
    diff = abs(num1 - num2)
    
    if num1 > num2:
        print(f"Number 1 ({num1}) is larger than Number 2 ({num2}).")
        print(f"Difference: {diff}")
    elif num2 > num1:
        print(f"Number 2 ({num2}) is larger than Number 1 ({num1}).")
        print(f"Difference: {diff}")
    else:
        print("Both numbers are equal.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    value_a = 42.5
    value_b = 108.7
    
    compare_numbers(value_a, value_b)