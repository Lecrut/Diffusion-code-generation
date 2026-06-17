def calculate_difference(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    try:
        num1_str = "15"
        num2_str = "7"
        num1 = float(num1_str)
        num2 = float(num2_str)
        difference = calculate_difference(num1, num2)
        print(f"The first number is: {num1}")
        print(f"The second number is: {num2}")
        print(f"The difference is: {difference}")
    except ValueError:
        print("Error: Invalid input. Please enter valid numeric values.")