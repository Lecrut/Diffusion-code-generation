def are_values_equal(a, b):
    return a == b

if __name__ == '__main__':
    value1 = "hello"
    value2 = "hello"
    value3 = "world"

    print(f"value1 equals value2: {are_values_equal(value1, value2)}")
    print(f"value1 equals value3: {are_values_equal(value1, value3)}")