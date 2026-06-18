# Command-line script to compare two numbers using conditional logic
def main():
    # Hard-coded sample values as per requirements (no user input)
    num1 = 42
    
    if __name__ == '__main__':
        num2 = 37
        
        print(f"Comparing {num1} and {num2}")
        
        is_greater = False
        
        # Conditional logic to determine if the first number is greater than the second
        if num1 > num2:
            is_greater = True
            
        result_message = "The first number is greater." if is_greater else \
                         "The first number is not greater."
        
        print(result_message)

if __name__ == '__main__':
    main()