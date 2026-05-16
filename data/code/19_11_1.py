def is_condition_true(a, b):
    return a == b
if __name__ == '__main__':
    result1 = is_condition_true(5, 5)
    print(result1)
    result2 = is_condition_true(10, 20)
    print(result2)
    result3 = is_condition_true("hello", "hello")
    print(result3)
    result4 = is_condition_true(3.14, 3.1400000000000004)
    print(result4)