def validate_input(a, b, c):
    if not all(isinstance(i, int) for i in (a, b, c)):
        raise ValueError("All inputs must be integers")
    return a, b, c

def sum_three_using_sum_function(a, b, c):
    numbers = validate_input(a, b, c)
    total = sum(numbers)
    return total

if __name__ == '__main__':
    num1, num2, num3 = 10, 20, 30
    result = sum_three_using_sum_function(num1, num2, num3)
    print(result)