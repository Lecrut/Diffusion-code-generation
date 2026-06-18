import sys

def main():
    # Hard-coded sample values as per requirements to avoid input() usage
    num1 = 42
    num2 = 50
    
    print(f"Comparing {num1} and {num2}")
    
    if num1 > num2:
        print("The first number is greater than the second.")
    else:
        print("The first number is not greater than the second.")

if __name__ == '__main__':
    main()