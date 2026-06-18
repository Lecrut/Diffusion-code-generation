def check_difference():
    """Check if two numbers differ from each other."""
    num1 = 10
    num2 = 25
    
    # Use absolute difference to handle negative numbers correctly
    diff = abs(num1 - num2)
    
    if diff != 0:
        print(f"The values {num1} and {num2} differ.")
    else:
        print(f"The values {num1} and {num2} do not differ.")

if __name__ == '__main__':
    check_difference()