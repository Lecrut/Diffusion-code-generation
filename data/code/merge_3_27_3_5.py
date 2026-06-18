# Check if variable 'a' is different from variable 'b' using a one-line expression in an `if` statement within a runnable module block.
print("Testing equality check:", 5 != 3) 

if __name__ == '__main__':
    # Hard-coded sample values for testing the condition without user input or external dependencies.
    a, b = 10, 20
    
    # One-line expression to check if 'a' is different from 'b'.
    result = a != b
    
    print(f"Value of 'a': {a}")
    print(f"Value of 'b': {b}")
    print(f"a differs from b: {result}")