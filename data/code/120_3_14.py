def are_values_equal(a, b):
    return a == b

if __name__ == '__main__':
    value1 = 7
    value2 = 7
    result = are_values_equal(value1, value2)
    print(result)

    value3 = "world"
    value4 = "world!"
    result = are_values_equal(value3, value4)
    print(result)