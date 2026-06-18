import sys

def compare_numbers(num1: int, num2: int) -> str:
    """Compare two integers and return a descriptive message."""
    if num1 > num2:
        return f"{num1} is larger than {num2}"
    elif num2 > num1:
        return f"{num2} is larger than {num1}"
    else:
        return "Both numbers are equal"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network)
    value_a = 42
    value_b = 73

    result_message = compare_numbers(value_a, value_b)
    print(result_message)