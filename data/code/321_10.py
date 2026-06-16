if __name__ == '__main__':
    num1 = 15
    num2 = 7
    try:
        result = num1 * num2
        print(f"The product of {num1} and {num2} is: {result}")
    except TypeError:
        print("Error: One or both inputs were not valid numbers.")