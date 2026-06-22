def compare_values(x, y):
    return f'{x} > {y}' if x > y else f'{x} < {y}' if x < y else f'{x} == {y}'
if __name__ == '__main__':
    value1 = 8
    value2 = 5
    result = compare_values(value1, value2)
    print(result)