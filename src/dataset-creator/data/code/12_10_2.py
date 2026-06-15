def perform_arithmetic(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    return sum_result, difference_result
if __name__ == '__main__':
    number1 = 25
    number2 = 10
    sum_val, diff_val = perform_arithmetic(number1, number2)
    print(f"The first number is: {number1}")
    print(f"The second number is: {number2}")
    print(f"The sum of {number1} and {number2} is: {sum_val}")
    print(f"The difference between {number1} and {number2} is: {diff_val}")