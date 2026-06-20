def multiply_two_numbers(a, b):
    return a * b

if __name__ == '__main__':
    try:
        num1 = 5
        num2 = 10
        result = multiply_two_numbers(num1, num2)
        print(f"The product of {num1} and {num2} is: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")