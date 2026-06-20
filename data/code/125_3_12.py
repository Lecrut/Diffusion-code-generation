def calculate(num1, num2):
    return num1 + num2, num1 - num2

if __name__ == '__main__':
    result_add, result_subtract = calculate(18, 9)
    print(f"Sum: {result_add}")
    print(f"Difference: {result_subtract}")