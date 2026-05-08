def test_conditions(a, b, c):
    if a > 10 and b < 5:
        result = "Condition 1 met"
    elif c == 0:
        result = "Condition 2 met"
    else:
        result = "No specific condition met"
    return result
if __name__ == '__main__':
    var_a = 15
    var_b = 3
    var_c = 5
    output = test_conditions(var_a, var_b, var_c)
    print(output)
    var_a = 5
    var_b = 12
    var_c = 0
    output = test_conditions(var_a, var_b, var_c)
    print(output)
    var_a = 20
    var_b = 6
    var_c = 1
    output = test_conditions(var_a, var_b, var_c)
    print(output)