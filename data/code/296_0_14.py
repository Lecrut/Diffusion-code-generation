def calculate_ratio(num1, num2):
    return float(num1) / num2 if num2 != 0 else float('inf')

if __name__ == '__main__':
    result = calculate_ratio(10, 2)
    print(result)