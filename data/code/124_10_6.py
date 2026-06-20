def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == '__main__':
    num1 = 8
    num2 = 3
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    sum_result = add(num1, num2)
    difference_result = subtract(num1, num2)
    product_result = multiply(num1, num2)
    quotient_result = divide(num1, num2)
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference_result}")
    print(f"Product: {product_result}")
    print(f"Quotient: {quotient_result}")