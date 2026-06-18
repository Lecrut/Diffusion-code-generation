import sys

def compare_numbers(a: int, b: int) -> None:
    """Compare two integers and print a descriptive message."""
    if a > b:
        msg = f"{a} is larger than {b}"
    elif b > a:
        msg = f"{b} is larger than {a}"
    else:
        msg = "The numbers are equal"
    sys.stdout.write(msg + "\n")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    num1, num2 = 42, 105
    
    try:
        compare_numbers(num1, num2)
    except Exception as e:
        sys.stdout.write(f"Error during comparison: {e}\n")