def perform_arithmetic(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    return addition, subtraction
if __name__ == '__main__':
    number1 = 25
    number2 = 10
    sum_result, difference_result = perform_arithmetic(number1, number2)
    print(f"The first number is: {number1}")
    print(f"The second number is: {number2}")
    print(f"The sum of {number1} and {number2} is: {sum_result}")
    print(f"The difference between {number1} and {number2} is: {difference_result}")