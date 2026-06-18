def multiply_and_divide(dividend, divisor):
    if divisor == 0:
        return "Error: Division by zero"
    result_multiplication = dividend * divisor
    result_division = dividend / divisor
    return result_multiplication, result_division
if __name__ == '__main__':
    a = 10
    b = 2
    print(multiply_and_divide(a, b))
    a = 15
    b = 3
    print(multiply_and_divide(a, b))
    a = 8
    b = 0
    print(multiply_and_divide(a, b))