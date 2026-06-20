def validate_input(*args):
    if not all(isinstance(arg, int) for arg in args):
        raise ValueError("All arguments must be integers")

def sum_three(a, b, c):
    validate_input(a, b, c)
    return sum((a, b, c))

if __name__ == '__main__':
    num1 = 10
    num2 = 20
    num3 = 30
    result = sum_three(num1, num2, num3)
    print(result)