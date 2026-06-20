def check_condition(x, y):
    return x and y
if __name__ == '__main__':
    result1 = check_condition(5, 3)
    print(result1)
    result2 = check_condition(0, 7)
    print(result2)
    result3 = check_condition(True, False)
    print(result3)
    result4 = check_condition(False, False)
    print(result4)