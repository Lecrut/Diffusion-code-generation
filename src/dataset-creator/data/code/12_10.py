def add_numbers(a, b):
    return a + b
def subtract_numbers(a, b):
    return a - b
if __name__ == '__main__':
    num1 = 25
    num2 = 10
    sum_result = add_numbers(num1, num2)
    difference_result = subtract_numbers(num1, num2)
    print(f"The first number is: {num1}")
    print(f"The second number is: {num2}")
    print(f"The sum of {num1} and {num2} is: {sum_result}")
    print(f"The difference between {num1} and {num2} is: {difference_result}")