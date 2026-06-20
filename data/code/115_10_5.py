def divide_numbers(dividend, divisor):
    if divisor == 0:
        return "Cannot divide by zero"
    return dividend / divisor

if __name__ == '__main__':
    num1 = 20.5
    num2 = 4.2
    result = divide_numbers(num1, num2)
    print(result)