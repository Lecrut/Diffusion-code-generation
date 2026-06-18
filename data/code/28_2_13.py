import sys

def compare_numbers(num1: int, num2: int) -> None:
    """
    Compares two integers and prints a descriptive message about their relationship.
    
    Parameters:
        num1 (int): First integer to compare.
        num2 (int): Second integer to compare.
    """
    if num1 > num2:
        print(f"{num1} is larger than {num2}")
    elif num2 > num1:
        print(f"{num2} is larger than {num1}")
    else:
        print("Both numbers are equal.")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, network access, or file reads are used.
    val_a = 42
    val_b = 57
    
    compare_numbers(val_a, val_b)