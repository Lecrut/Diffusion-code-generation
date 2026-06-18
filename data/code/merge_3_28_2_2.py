import sys

def compare_numbers(a: int, b: int) -> str:
    """Compare two integers and return a descriptive message."""
    if a > b:
        return f"{a} is larger than {b}"
    elif b > a:
        return f"{b} is larger than {a}"
    else:
        return "Both numbers are equal"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    num1 = 42
    num2 = 7
    
    result_message = compare_numbers(num1, num2)
    
    print(result_message)