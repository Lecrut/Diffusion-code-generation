def calculate_arithmetic():
    a = 5
    b = 3
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b
    remainder_result = a % b
    return sum_result, difference_result, product_result, quotient_result, remainder_result

if __name__ == '__main__':
    results = calculate_arithmetic()
    print("Sum:", results[0])
    print("Difference:", results[1])
    print("Product:", results[2])
    print("Quotient:", results[3])
    print("Remainder:", results[4])