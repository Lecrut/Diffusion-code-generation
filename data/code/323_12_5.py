def calculate_difference(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    try:
        num1 = 15
        num2 = 7
        difference = calculate_difference(num1, num2)
        print(f"The first number is: {num1}")
        print(f"The second number is: {num2}")
        print(f"The difference between the two numbers is: {difference}")
    except TypeError:
        print("Error: One or both inputs were not valid numbers.")