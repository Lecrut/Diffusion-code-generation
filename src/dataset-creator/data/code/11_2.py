import math
def calculate_operations(a, b):
    average = (a + b) / 2.0
    difference = abs(a - b)
    product = a * b
    quotient = a / b if b != 0 else float('inf')
    return average, difference, product, quotient
if __name__ == '__main__':
    num1 = 10.5
    num2 = 4.0
    avg, diff, prod, quot = calculate_operations(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Average: {avg}")
    print(f"Difference: {diff}")
    print(f"Product: {prod}")
    print(f"Quotient: {quot}")