def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")

def sum_ab(a, b):
    validate_numbers(a, b)
    return a + b

if __name__ == '__main__':
    num1 = 4
    num2 = 6
    print(sum_ab(num1, num2))