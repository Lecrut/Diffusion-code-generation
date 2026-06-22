def calculate_sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    return a + b

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    total_sum = calculate_sum(num1, num2)
    print(total_sum)