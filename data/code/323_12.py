if __name__ == '__main__':
    num1 = 15
    num2 = 7
    try:
        difference = num1 - num2
        print(f"The first number is: {num1}")
        print(f"The second number is: {num2}")
        print(f"The difference is: {difference}")
    except TypeError:
        print("Error: One or both inputs were not valid numbers.")