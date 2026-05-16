import math
def calculate_stats(a: float, b: float) -> tuple:
    sum_val = a + b
    diff_val = a - b
    prod_val = a * b
    div_val = a / b
    return (sum_val, diff_val, prod_val, div_val)
if __name__ == '__main__':
    num1 = 10.5
    num2 = 2.0
    results = calculate_stats(num1, num2)
    print(results)