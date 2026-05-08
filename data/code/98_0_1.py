def test_conditions(a, b, c):
    if a > 10 and b < 5:
        result = "Condition 1 met"
    elif c == 0:
        result = "Condition 2 met"
    else:
        result = "No specific condition met"
    return result
if __name__ == '__main__':
    x = 15
    y = 3
    z = 5
    output = test_conditions(x, y, z)
    print(output)