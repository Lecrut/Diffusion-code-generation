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
        print(f"The difference between them is {diff}.")
    elif num2 > num1:
        print(f"Number 2 ({num2}) is larger than Number 1 ({num1}).")
        print(f"The absolute difference between them is {diff}.")
    else:
        print("Both numbers are equal.")
        print(f"The difference between them is {diff} (zero).")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access used here.
    value_a = 10.5
    value_b = 7.2
    
    compare_numbers(value_a, value_b)