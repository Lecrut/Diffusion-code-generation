MAX_A = 10
MIN_B = 5
ZERO_C = 0

def test_conditions(a, b, c):
    if a > MAX_A and b < MIN_B:
        result = "Condition 1 met"
    elif c == ZERO_C:
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
    var_b = 8
    var_c = 0
    output = test_conditions(var_a, var_b, var_c)
    print(output)