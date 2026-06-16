if __name__ == '__main__':
    num1 = 25
    num2 = 10
    try:
        result = num1 - num2
        print(result)
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")