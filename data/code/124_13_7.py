def calculate():
    a = 10
    b = 5
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b
    return sum_result, difference_result, product_result, quotient_result

if __name__ == '__main__':
    results = calculate()
    print("Sum:", results[0])
    print("Difference:", results[1])
    print("Product:", results[2])
    print("Quotient:", results[3])