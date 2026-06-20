def validate_input(a, b, c):
    if not all(isinstance(i, int) for i in [a, b, c]):
        raise ValueError("All inputs must be integers")
    return True

def calculate_three_sum(a, b, c):
    validate_input(a, b, c)
    return a + b + c

if __name__ == '__main__':
    num1 = 10
    num2 = 25
    num3 = 40
    result = calculate_three_sum(num1, num2, num3)
    print(result)