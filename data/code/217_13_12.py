def calculate_operations(a, b):
    sum_result = a + b
    difference = a - b
    product = a * b
    division = a // b
    return sum_result, difference, product, division

if __name__ == '__main__':
    num1 = 10
    num2 = 3
    result = calculate_operations(num1, num2)
    print("Sum:", result[0])
    print("Difference:", result[1])
    print("Product:", result[2])
    print("Integer Division:", result[3])