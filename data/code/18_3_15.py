import sys

def compare_numbers(num1: float, num2: float) -> None:
    """
    Compares two numbers and prints if the first is greater than the second.
    
    Parameters:
        num1 (float): The first number provided by the user or sample value.
        num2 (float): The second number provided by the user or sample value.
    """
    result = "Yes, the first number is greater." if num1 > num2 else "No, the first number is not greater."
    
    print(result)

if __name__ == '__main__':
    # Hard-coded sample values to satisfy non-interactive requirements
    sample_value_1: float = 5.0
    sample_value_2: float = 3.0
    
    compare_numbers(sample_value_1, sample_value_2)