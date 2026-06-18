import sys

def compare_numbers(a: int, b: int) -> str:
    """Compare two integers and return a descriptive message."""
    if a > b:
        return f"{a} is larger than {b}"
    elif b > a:
        return f"{b} is larger than {a}"
    else:
        return f"{a} is equal to {b}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirement (no user input, args, or network)
    num1 = 42
    num2 = 97
    
    result_message = compare_numbers(num1, num2)
    
    print(result_message)