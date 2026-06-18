# Command-line script to compare two numbers using conditional logic
def main():
    # Hard-coded sample values as per requirements (no user input)
    num1 = 42
    num2 = 37
    
    print(f"Comparing {num1} and {num2}")

    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    else:
        print(f"{num1} is not greater than {num2}.")

if __name__ == '__main__':
    main()