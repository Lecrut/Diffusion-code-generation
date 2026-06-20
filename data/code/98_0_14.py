def test_conditions(a, b, c):
    if a > 0 and b < 0:
        return "A is positive and B is negative"
    elif a == 0 or b == 0:
        return "A or B is zero"
    else:
        return "Neither condition met"

if __name__ == '__main__':
    print(test_conditions(5, -3, 2))
    print(test_conditions(0, 4, 1))
    print(test_conditions(-1, 6, 3))