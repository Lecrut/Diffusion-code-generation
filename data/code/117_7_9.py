def subtract_numbers(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise ValueError('Both inputs must be numbers')

if __name__ == '__main__':
    num1 = 30.5
    num2 = 15.2
    result = subtract_numbers(num1, num2)
    print(result)