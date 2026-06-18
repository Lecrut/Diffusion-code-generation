import sys

def compare_values(a: float, b: float) -> str:
    """Compare two numerical values and return a string indicating which is larger."""
    if a > b:
        return "Value A is larger"
    elif b > a:
        return "Value B is larger"
    else:
        return "Values are equal"

def main():
    # Hard-coded sample values as per requirements to avoid user input or command-line arguments.
    value_a = 10.5
    value_b = 20.3

    result = compare_values(value_a, value_b)
    print(result)

if __name__ == '__main__':
    main()