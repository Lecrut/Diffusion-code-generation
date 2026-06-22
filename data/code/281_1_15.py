def calculate_sum(a, b, c, d):
    try:
        result = a + b + c + d
        return round(result, 2)
    except TypeError as e:
        raise ValueError("All inputs must be numbers") from e

if __name__ == '__main__':
    data = (1.2345, 6.7890, 2.3456, 3.4567)
    try:
        result = calculate_sum(*data)
        print(result)
    except ValueError as e:
        print(e)