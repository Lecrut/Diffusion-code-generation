if __name__ == '__main__':
    num1 = 15.7
    num2 = 8.3
    try:
        result = num1 - num2
        print(result)
    except TypeError:
        print("Error: Invalid input types.")