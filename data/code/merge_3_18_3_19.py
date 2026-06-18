import sys

def compare_numbers(a: float, b: float) -> bool:
    """Check if number a is greater than number b."""
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    num1 = 42
    num2 = 38

    result = compare_numbers(num1, num2)

    if result:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num1} is not greater than {num2}")