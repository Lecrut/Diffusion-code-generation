import sys
if __name__ == '__main__':
    num1 = 10.5
    num2 = 4.0
    average = (num1 + num2) / 2
    difference = abs(num1 - num2)
    product = num1 * num2
    quotient = num1 / num2 if num2 != 0 else float('inf')
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Average: {average}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Quotient: {quotient}")