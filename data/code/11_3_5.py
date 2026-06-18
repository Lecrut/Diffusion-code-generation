import sys

def calculate_ratio(a: float, b: float) -> None:
    """Calculates and prints the ratio of two lengths."""
    if a == 0 or b == 0:
        print("Error: Cannot divide by zero. At least one length is zero.")
        return
    
    ratio = a / b
    print(f"The ratio of {a} to {b} is {ratio:.4f}")

def main():
    # Hard-coded sample values as per task requirements
    length_a = 10.5
    length_b = 20.0

    calculate_ratio(length_a, length_b)

if __name__ == '__main__':
    main()