def test_conditions(a, b, c):
    if a > 0 and b < 0:
        return "A is positive and B is negative"
    elif c == True and a != b:
        return "C is true and A is not equal to B"
    else:
        return "None of the conditions are met"

if __name__ == '__main__':
    print(test_conditions(5, -3, True))