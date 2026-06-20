def sum_three_numbers(x: float, y: float, z: float) -> float:
    intermediate_sum = x + y
    final_result = intermediate_sum + z
    return final_result

if __name__ == '__main__':
    num1 = 1.23456789
    num2 = 9.87654321
    num3 = -10.0
    result = sum_three_numbers(num1, num2, num3)
    print(result)