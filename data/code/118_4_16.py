from functools import mul

def calculate_multiplication(num1, num2):
    return mul(num1, num2)

if __name__ == '__main__':
    first_number = 8
    second_number = 5
    multiplication_result = calculate_multiplication(first_number, second_number)
    print(multiplication_result)