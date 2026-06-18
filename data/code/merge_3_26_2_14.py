def main():
    # Simulate user input with hard-coded sample values as per requirements
    num1 = 42
    num2 = 9
    
    print(f"Comparing {num1} and {num2}")
    
    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    else:
        # Note: The task specifically asks to check if the first number is GREATER.
        # If they are not, we simply do nothing or could add a message indicating it wasn't found as per implied logic flow.
        print(f"{num1} was NOT greater than {num2}.")

if __name__ == '__main__':
    main()