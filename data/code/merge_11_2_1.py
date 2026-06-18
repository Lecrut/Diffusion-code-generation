import math
def calculate_operations(num1, num2):
    average = (num1 + num2) / 2
    difference = abs(num1 - num2)
    product = num1 * num2
    quotient = num1 / num2 if num2 != 0 else float('inf')
    return average, difference, product, quotient
if __name__ == '__main__':
    a = 10.5
    b = 4.0
    avg, diff, prod, quot = calculate_operations(a, b)
    print(f"Number 1: {a}")
    print(f"Number 2: {b}")
    print(f"Average: {avg}")
    print(f"Difference: {diff}")
    print(f"Product: {prod}")
    print(f"Quotient: {quot}")