def validate_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers")
    return True

def calculate_sum(num1, num2):
    validate_integers(num1, num2)
    sum_result = num1 + num2
    return sum_result

if __name__ == '__main__':
    result = calculate_sum(15, 27)
    print(result)