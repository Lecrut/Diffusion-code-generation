def calculate_sum_difference(a: int, b: int) -> (int, int):
    return (a + b, a - b)

if __name__ == '__main__':
    num1 = 10
    num2 = 4
    result = calculate_sum_difference(num1, num2)
    print(result)