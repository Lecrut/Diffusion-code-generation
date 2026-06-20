if __name__ == '__main__':
    num1 = 20
    num2 = 4
    try:
        result = num1 / num2
        print(f"Result of {num1} divided by {num2}: {result}")
    except ZeroDivisionError as e:
        print(e)