def compare_values(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both arguments must be int or float')
    return (a > b) - (a < b)
if __name__ == '__main__':
    try:
        result1 = compare_values(7, 3)
        print(result1)
        result2 = compare_values(4, 4)
        print(result2)
        result3 = compare_values(9, 15)
        print(result3)
        result4 = compare_values('a', 5)
    except ValueError as e:
        print(e)