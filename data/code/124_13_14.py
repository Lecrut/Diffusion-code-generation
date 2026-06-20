def calculate():
    a = 5
    b = 3
    sum_result = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    remainder = a % b
    return sum_result, difference, product, quotient, remainder

if __name__ == '__main__':
    results = calculate()
    print("Sum:", results[0])
    print("Difference:", results[1])
    print("Product:", results[2])
    print("Quotient:", results[3])
    print("Remainder:", results[4])