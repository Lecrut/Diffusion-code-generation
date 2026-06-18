# Command-line script to compare two numbers using conditional logic

def main():
    # Hard-coded sample values as per requirements (no user input)
    num1 = 45
    num2 = 30
    
    print(f"Comparing {num1} and {num2}")
    
    if num1 > num2:
        result_message = f"{num1} is greater than {num2}"
    else:
        result_message = f"{num1} is not greater than {num2}"
        
    print(result_message)

if __name__ == '__main__':
    main()