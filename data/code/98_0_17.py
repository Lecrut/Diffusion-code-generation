def test_conditions(a, b, c):
    if a > 0 and b < 0 and (c == 0):
        return 'Condition 1'
    elif a == 0 or b == 0 or c == 0:
        return 'Condition 2'
    else:
        return 'Condition 3'
if __name__ == '__main__':
    print(test_conditions(1, -1, 0))
    print(test_conditions(0, 0, 0))
    print(test_conditions(1, 1, 1))