def compare_numbers(num1: float, num2: float) -> None:
    """
    Compares two numbers and prints a formatted report detailing 
    their difference and which one is larger.
    
    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
    """
    diff = abs(num1 - num2)
    
    if num1 > num2:
        print(f"Number 1 ({num1}) is larger than Number 2 ({num2}).")
        print(f"The absolute difference between them is {diff:.4f}.")
    elif num2 > num1:
        print(f"Number 2 ({num2}) is larger than Number 1 ({num1}).")
        print(f"The absolute difference between them is {diff:.4f}.")
    else:
        print("Both numbers are equal.")
        print(f"The difference between them is exactly 0.0000.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    value_a = 15.732
    value_b = 8.49
    
    compare_numbers(value_a, value_b)