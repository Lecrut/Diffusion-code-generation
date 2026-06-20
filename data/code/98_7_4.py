STATE_MAP = {
    'A': 1,
    'B': 2,
    'C': 4,
    'D': 8
}

def system_state_checker(flag_a, flag_b, flag_c, flag_d):
    state = 0
    if flag_a:
        state |= STATE_MAP['A']
    if flag_b:
        state |= STATE_MAP['B']
    if flag_c:
        state |= STATE_MAP['C']
    if flag_d:
        state |= STATE_MAP['D']
    return state

if __name__ == '__main__':
    a = True
    b = False
    c = True
    d = True
    result = system_state_checker(a, b, c, d)
    print(result)