SUM_CONSTANT = 100
DIFF_CONSTANT = 50

def calculate_sum_difference(a: int, b: int) -> (int, int):
    return a + b, a - b

if __name__ == '__main__':
    num1 = SUM_CONSTANT // 2
    num2 = DIFF_CONSTANT // 2
    result = calculate_sum_difference(num1, num2)
    print(result)