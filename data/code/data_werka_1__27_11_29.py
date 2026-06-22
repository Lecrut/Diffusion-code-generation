def are_values_distinct(a, b):
    return not math.isclose(a, b)

if __name__ == '__main__':
    value1 = 10
    value2 = 10.00000000000001
    print(are_values_distinct(value1, value2))