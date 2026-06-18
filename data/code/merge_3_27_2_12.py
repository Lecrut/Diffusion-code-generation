def main():
    # Hard-coded sample values to ensure the script runs without user input
    num1 = 5
    num2 = 3
    
    print(f"Comparing number {num1} and {num2}.")
    
    if num1 != num2:
        message = "The two entered values differ."
    else:
        message = "The two entered values are the same."
        
    print(message)

if __name__ == '__main__':
    main()