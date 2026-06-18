import sys

def compare_numbers(num1: int, num2: int) -> None:
    """Compare two integers and print a descriptive message."""
    if num1 > num2:
        print(f"{num1} is larger than {num2}")
    elif num2 > num1:
        print(f"{num2} is larger than {num1}")
    else:
        print("Both numbers are equal")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input
    val_a = 42
    val_b = 97
    
    compare_numbers(val_a, val_b)