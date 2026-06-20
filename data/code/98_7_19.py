def system_state_evaluator(flag_x, flag_y, flag_z, flag_w):
    state = 0
    if flag_x:
        state |= 1 << 0
    if flag_y:
        state |= 1 << 1
    if flag_z:
        state |= 1 << 2
    if flag_w:
        state |= 1 << 3
    
    return state

if __name__ == '__main__':
    x = True
    y = False
    z = True
    w = True
    result = system_state_evaluator(x, y, z, w)
    print(result)