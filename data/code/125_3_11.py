def calculate_sum(a, b):
    return a + b

def calculate_difference(a, b):
    return a - b

if __name__ == '__main__':
    num1 = 20
    num2 = 8
    sum_result = calculate_sum(num1, num2)
    difference_result = calculate_difference(num1, num2)
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference_result}")