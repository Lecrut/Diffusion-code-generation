def check_condition(a, b, c):
    if a > 0 and b % 2 == 0 and c % (a * b) == 0:
        return True
    return False
if __name__ == '__main__':
    result1 = check_condition(2, 4, 8)
    print(result1)
    result2 = check_condition(3, 6, 12)
    print(result2)
    result3 = check_condition(1, 2, 4)
    print(result3)
    result4 = check_condition(5, 10, 20)
    print(result4)
    result5 = check_condition(1, 3, 12)
    print(result5)