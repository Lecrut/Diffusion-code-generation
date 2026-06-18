def compare_numbers(num1: int, num2: int) -> None:
    """Prints whether the first number is greater than the second."""
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num1} is not greater than {num2}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid user input or prompts
    num_a = 50
    num_b = 30
    
    compare_numbers(num_a, num_b)