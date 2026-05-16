def check_condition(a, b, c):
    if a > 0 and b % 2 == 0 and c % (a * b) == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    result1 = check_condition(3, 4, 12)
    print(result1)
    result2 = check_condition(5, 6, 30)
    print(result2)
    result3 = check_condition(2, 4, 10)
    print(result3)
    result4 = check_condition(1, 2, 5)
    print(result4)