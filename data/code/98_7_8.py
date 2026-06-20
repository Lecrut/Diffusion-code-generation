FLAG_A = 1
FLAG_B = 2
FLAG_C = 4
FLAG_D = 8

def system_state_checker(flag_a, flag_b, flag_c, flag_d):
    state = 0
    if flag_a:
        state |= FLAG_A
    if flag_b:
        state |= FLAG_B
    if flag_c:
        state |= FLAG_C
    if flag_d:
        state |= FLAG_D
    return state
if __name__ == '__main__':
    a = True
    b = False
    c = True
    d = True
    result = system_state_checker(a, b, c, d)
    print(result)