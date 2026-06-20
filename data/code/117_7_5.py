def subtract_numbers(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return float(a - b)
    else:
        raise ValueError('Both inputs must be numbers')

if __name__ == '__main__':
    num1 = 20.5
    num2 = 7.3
    result = subtract_numbers(num1, num2)
    print(result)