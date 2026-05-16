def divide_two_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b
if __name__ == '__main__':
    print(divide_two_numbers(10.0, 2.0))
    print(divide_two_numbers(10.0, 0.0))
    print(divide_two_numbers(-15.0, 3.0))
    print(divide_two_numbers(7.0, 0.0))