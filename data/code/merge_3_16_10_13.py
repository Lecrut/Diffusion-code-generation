import sys

def is_positive(value):
    """Check if a given integer value is positive."""
    return value > 0

def main():
    # Hard-coded sample values to demonstrate functionality without user input or CLI args
    test_values = [5, -3, 0]
    
    for val in test_values:
        result = "Positive" if is_positive(val) else "Non-positive (zero or negative)"
        print(f"{val} -> {result}")

if __name__ == '__main__':
    main()