def calculate_state(flag_a, flag_b, flag_c, flag_d):
    state = 0
    if flag_a:
        state |= 1
    if flag_b:
        state |= 2
    if flag_c:
        state |= 4
    if flag_d:
        state |= 8
    return state

def system_state_checker(flag_a, flag_b, flag_c, flag_d):
    state = calculate_state(flag_a, flag_b, flag_c, flag_d)
    if state == 0:
        result = "OFF"
    elif state == 15:
        result = "FULL ON"
    else:
        result = "PARTIAL ON"
    return result

if __name__ == '__main__':
    a = True
    b = False
    c = True
    d = True
    result = system_state_checker(a, b, c, d)
    print(result)