if __name__ == '__main__':
    num1 = 15.5
    num2 = 7.2
    try:
        result = num1 - num2
        print(result)
    except TypeError:
        print("Error: Invalid input types.")