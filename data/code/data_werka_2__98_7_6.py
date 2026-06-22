def evaluate_system_state(flag_a, flag_b, flag_c, flag_d):
    a = 1 if flag_a else 0
    b = 1 if flag_b else 0
    c = 1 if flag_c else 0
    d = 1 if flag_d else 0
    if a & b & c & d == 1:
        return 1
    count = a + b + c + d
    if a == 1 and count >= 2:
        return 2
    if b == 1 and c == 1 and (d == 0):
        return 3
    if a == 1 and b == 0:
        return 4
    return 0
if __name__ == '__main__':
    result1 = evaluate_system_state(True, True, True, True)
    print(result1)
    result2 = evaluate_system_state(True, True, False, False)
    print(result2)
    result3 = evaluate_system_state(False, True, True, False)
    print(result3)
    result4 = evaluate_system_state(True, False, False, False)
    print(result4)
    result5 = evaluate_system_state(False, False, False, False)
    print(result5)
    result6 = evaluate_system_state(True, False, False, True)
    print(result6)
    result7 = evaluate_system_state(False, True, False, True)
    print(result7)