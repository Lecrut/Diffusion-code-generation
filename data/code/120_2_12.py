def are_values_equal(a, b):
    return a == b

if __name__ == '__main__':
    value1 = 25
    value2 = "25"
    print(f"{value1} == {value2}: {are_values_equal(value1, value2)}")