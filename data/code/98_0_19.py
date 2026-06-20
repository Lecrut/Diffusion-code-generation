def test_conditions(a, b, c):
    if a > 0 and b < 0:
        return "A is positive and B is negative"
    elif c == True:
        return "C is true"
    else:
        return "None of the conditions are met"

if __name__ == '__main__':
    print(test_conditions(5, -3, True))