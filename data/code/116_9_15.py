def sum_three_numbers(a, b, c):
    if not all((isinstance(i, (int, float)) for i in [a, b, c])):
        raise ValueError('All inputs must be numeric (int or float) to calculate the sum.')
    return a + b + c
if __name__ == '__main__':
    print(sum_three_numbers(10, 5.5, 2))
    try:
        print(sum_three_numbers('a', 5, 3))
    except ValueError as e:
        print(e)