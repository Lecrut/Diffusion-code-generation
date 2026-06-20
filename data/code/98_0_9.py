def test_conditions(a, b, c):
    if a > 0 and b < 0:
        return "Condition 1 met"
    elif c == True and a != b:
        return "Condition 2 met"
    else:
        return "No conditions met"

if __name__ == '__main__':
    print(test_conditions(5, -3, True))
    print(test_conditions(-1, 2, False))
    print(test_conditions(0, 0, True))