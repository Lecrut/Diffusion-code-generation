def are_values_equal(a, b):
    return a == b

if __name__ == '__main__':
    value1 = 5
    value2 = 5
    print(f"value1: {value1}, value2: {value2}, equal: {are_values_equal(value1, value2)}")

    value3 = "hello"
    value4 = "hello"
    print(f"value3: \"{value3}\", value4: \"{value4}\", equal: {are_values_equal(value3, value4)}")

    value5 = [1, 2, 3]
    value6 = [1, 2, 3]
    print(f"value5: {value5}, value6: {value6}, equal: {are_values_equal(value5, value6)}")