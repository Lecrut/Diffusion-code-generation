# Check if 'num' is even using the modulo operator within a boolean context
result = num % 2 == 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    test_cases = [4, -3, 0]
    for val in test_cases:
        print(f"Is {val} even? {(val % 2 == 0)}")