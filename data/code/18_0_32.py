def is_strictly_greater(a, b):
    try:
        return float(a) > float(b)
    except ValueError:
        raise ValueError("Both inputs must be numbers")

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result = is_strictly_greater(num1, num2)
    print(result)