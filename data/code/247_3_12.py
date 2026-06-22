if __name__ == '__main__':
    num1 = 3
    num2 = 7
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both inputs must be numbers")
    result = num1 + num2
    print(result)