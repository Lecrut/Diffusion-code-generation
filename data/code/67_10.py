if __name__ == '__main__':
    num1 = 15
    num2 = 27
    try:
        sum_result = num1 + num2
        print(sum_result)
    except TypeError:
        print("Error: One or both inputs were not valid numbers.")