import sys

def compare_numbers(num1: float, num2: float) -> str:
    """
    Compare two numbers and return a formatted report of their difference 
    and which one is larger.
    
    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
        
    Returns:
        str: A string containing the comparison result and difference information.
    """
    difference = abs(num1 - num2)
    if num1 > num2:
        larger, smaller = f"{num1}", f"{num2}"
        message = "The first number is larger."
    elif num2 > num1:
        larger, smaller = f"{num2}", f"{num1}"
        message = "The second number is larger."
    else:
        larger, smaller = equal_message(num1)

    report = (f"Difference between the two values: {difference}\n" 
              f"Larger value: {larger}\n"
              f"Smaller value: {smaller}\n" + message.lstrip())
    
    return report

def equal_message(value):
    """Helper to handle equal numbers"""
    msg = "Both values are equal."
    if isinstance(value, float) and (int(value) == value):
        str_value = f"{value} ({float(int(value))})"
    else:
        str_value = value
    
    return f"Larger value: {str_value}\nSmaller value: {str_value}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    num1 = 25.75
    num2 = 30.49
    
    print(compare_numbers(num1, num2))