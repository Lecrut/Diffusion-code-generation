import sys

def compare_numbers(num1: float, num2: float) -> None:
    """
    Compare two numbers and print a formatted report detailing their difference 
    and which one is larger.
    
    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
    """
    if num1 == num2:
        diff_msg = "The numbers are equal."
        greater_msg = "Neither number is larger."
    elif num1 > num2:
        difference = round(num1 - num2, 4)
        diff_msg = f"The first number ({num1}) exceeds the second by {difference}."
        greater_msg = f"{num1} is larger than {num2}."
    else:
        difference = round(num2 - num1, 4)
        diff_msg = f"The second number ({num2}) exceeds the first by {difference}."
        greater_msg = f"{num2} is larger than {num1}."

    print(f"Comparison Report")
    print("-" * 30)
    print(f"Value A: {num1}")
    print(f"Value B: {num2}")
    print(diff_msg)
    print(greater_msg)

if __name__ == '__main__':
    # Hard-coded sample values for execution without user input or external dependencies.
    sample_value_a = 450.789123
    sample_value_b = 450.100
    
    compare_numbers(sample_value_a, sample_value_b)