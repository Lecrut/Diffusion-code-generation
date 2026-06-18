import sys

def compare_numbers(a: int, b: int) -> None:
    """Compare two integers and print a descriptive message."""
    if a > b:
        print(f"{a} is larger than {b}")
    elif b > a:
        print(f"{b} is larger than {a}")
    else:
        print("The numbers are equal")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid any input prompts or dependencies.
    num1 = 42
    num2 = 99
    
    compare_numbers(num1, num2)