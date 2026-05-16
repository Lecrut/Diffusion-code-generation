if __name__ == '__main__':
    num1 = 15.5
    num2 = 22.3
    try:
        if num1 > num2:
            print(f"{num1} is greater than {num2}")
        elif num2 > num1:
            print(f"{num2} is greater than {num1}")
        else:
            print(f"{num1} and {num2} are equal")
    except ValueError:
        print("An error occurred: Invalid input. Please enter valid numbers.")