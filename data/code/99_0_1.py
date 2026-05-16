def calculate_expression(a, b, c, d):
    result = a + b * c - d / 2
    result = result // 3 + a % b
    result = result ** 2
    return result
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 3
    num4 = 2
    final_result = calculate_expression(num1, num2, num3, num4)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Number 3: {num3}")
    print(f"Number 4: {num4}")
    print(f"Final Result of the nested expression: {final_result}")