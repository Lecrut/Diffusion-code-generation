def check_condition(x, y):
    return x & y
if __name__ == '__main__':
    result1 = check_condition(5, 3)
    print(result1)
    result2 = check_condition(10, 10)
    print(result2)
    result3 = check_condition(2, 7)
    print(result3)
    result4 = check_condition(-1, 0)
    print(result4)