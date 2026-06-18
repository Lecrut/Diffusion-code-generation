def compare_numbers():
    """Function to prompt for two numbers (simulated via hard-coded values) 
    and determine if the first is greater than the second."""
    
    # Hard-coded sample values as per requirements
    num1 = 25
    num2 = 30
    
    print(f"Comparing {num1} with {num2}")
    
    # Conditional logic to check if first number is greater than the second
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num1} is not greater than {num2}")

if __name__ == '__main__':
    compare_numbers()