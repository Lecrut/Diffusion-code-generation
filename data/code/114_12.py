if __name__ == '__main__':
    num1 = 10
    num2 = 5
    try:
        result = num1 * num2
        print(result)
    except TypeError:
        print("Error: One or both inputs were not valid numbers.")