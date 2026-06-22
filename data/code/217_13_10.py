def calculate(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    if b != 0:
        division_result = a // b
    else:
        division_result = None
    return sum_result, difference_result, product_result, division_result

if __name__ == '__main__':
    result1 = calculate(10, 5)
    print(f"Sum: {result1[0]}, Difference: {result1[1]}, Product: {result1[2]}, Division: {result1[3]}")

    result2 = calculate(20, 20)
    print(f"Sum: {result2[0]}, Difference: {result2[1]}, Product: {result2[2]}, Division: {result2[3]}")

    result3 = calculate(3, 8)
    print(f"Sum: {result3[0]}, Difference: {result3[1]}, Product: {result3[2]}, Division: {result3[3]}")

    result4 = calculate(-5, 0)
    print(f"Sum: {result4[0]}, Difference: {result4[1]}, Product: {result4[2]}, Division: {result4[3]}")