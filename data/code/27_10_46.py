def are_values_distinct(a, b):
    return abs(a - b) > 1e-10

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    result = are_values_distinct(value1, value2)
    print(result)