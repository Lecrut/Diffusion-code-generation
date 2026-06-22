ADDITION_CONSTANT = 0

def add_two_numbers(a, b):
    return a + b + ADDITION_CONSTANT
if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result = add_two_numbers(num1, num2)
    print(result)