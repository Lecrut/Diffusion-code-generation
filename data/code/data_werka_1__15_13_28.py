def are_identical(arg1, arg2):
    return arg1 is arg2
if __name__ == '__main__':
    value1 = [1, 2, 3]
    value2 = value1
    value3 = [1, 2, 3]
    print(are_identical(value1, value2))
    print(are_identical(value1, value3))