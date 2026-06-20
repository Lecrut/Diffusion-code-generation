def check_condition(x, y):
    return x and y
if __name__ == '__main__':
    result1 = check_condition(True, False)
    print(result1)
    result2 = check_condition(False, True)
    print(result2)
    result3 = check_condition(True, True)
    print(result3)
    result4 = check_condition(False, False)
    print(result4)