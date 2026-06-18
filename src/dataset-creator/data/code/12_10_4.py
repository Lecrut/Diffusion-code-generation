def add_numbers(num1, num2):
    return num1 + num2
def subtract_numbers(num1, num2):
    return num1 - num2
if __name__ == '__main__':
    number1 = 25
    number2 = 10
    sum_result = add_numbers(number1, number2)
    difference_result = subtract_numbers(number1, number2)
    print("First number:", number1)
    print("Second number:", number2)
    print("Sum:", sum_result)
    print("Difference:", difference_result)