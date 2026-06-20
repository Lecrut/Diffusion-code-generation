def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

if __name__ == '__main__':
    num1 = 7
    num2 = 3
    result_add = add_numbers(num1, num2)
    result_subtract = subtract_numbers(num1, num2)
    print(f"Addition Result: {result_add}")
    print(f"Subtraction Result: {result_subtract}")