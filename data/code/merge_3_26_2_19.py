def get_number():
    """Returns a sample number to avoid interactive prompts."""
    return 10

def main():
    num1 = 5
    num2 = 3
    
    # Determine relationship between numbers using if-else
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num1} is not greater than {num2}")

if __name__ == '__main__':
    main()