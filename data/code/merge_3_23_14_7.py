import sys

def compare_numbers(num1: float, num2: float) -> None:
    """
    Compares two numbers and prints a formatted report detailing 
    their difference and which one is larger.
    
    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
    """
    diff = abs(num1 - num2)
    
    print(f"Number 1 ({num1}) vs Number 2 ({num2}):")
    print("-" * 30)
    print(f"Difference: {diff:.4f}")
    
    if num1 > num2:
        larger = "First number is larger."
    elif num2 > num1:
        larger = "Second number is larger."
    else:
        larger = "Both numbers are equal."
        
    print(larger)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args needed)
    value_a = 10.5
    value_b = 23.7
    
    compare_numbers(value_a, value_b)