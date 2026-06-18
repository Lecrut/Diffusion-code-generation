def check_number(n):
    """Check if a number is negative."""
    return n < 0

if __name__ == '__main__':
    test_values = [1, -5, 0]
    
    for value in test_values:
        result = check_number(value)
        
        if result:
            print(f"The entered value {value} is negative.")
        else:
            print(f"The entered value {value} is not negative.")