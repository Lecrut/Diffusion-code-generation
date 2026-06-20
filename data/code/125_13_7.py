SUM_CONSTANT = 1
DIFF_CONSTANT = -1

def calculate_sum_difference(a, b):
    return (a + b * SUM_CONSTANT, a + b * DIFF_CONSTANT)
if __name__ == '__main__':
    num1 = 20
    num2 = 5
    result = calculate_sum_difference(num1, num2)
    print(result)