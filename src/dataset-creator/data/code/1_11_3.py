if __name__ == '__main__':
    num1 = 10.5
    num2 = 3.2
    try:
        result = num1 - num2
        print(result)
    except ValueError:
        print("Error: Invalid input provided.")