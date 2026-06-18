if __name__ == '__main__':
    num1 = 10
    num2 = 25
    num3 = 7
    try:
        sum_result = num1 + num2 + num3
        print(sum_result)
    except TypeError:
        print("Error: One or more inputs were not valid numbers.")