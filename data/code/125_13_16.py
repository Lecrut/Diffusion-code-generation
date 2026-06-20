def calculate_sum_and_difference(a: int, b: int) -> tuple:
    return a + b, a - b

if __name__ == '__main__':
    result = calculate_sum_and_difference(5, 3)
    print(result)