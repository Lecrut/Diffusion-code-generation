def system_state_checker(flag_a: bool, flag_b: bool, flag_c: bool, flag_d: bool) -> int:
    state = 0
    if not all(isinstance(f, bool) for f in [flag_a, flag_b, flag_c, flag_d]):
        raise ValueError("All inputs must be boolean.")
    
    if flag_a:
        state |= 1
    if flag_b:
        state |= 2
    if flag_c:
        state |= 4
    if flag_d:
        state |= 8
    
    return state

if __name__ == '__main__':
    a = True
    b = False
    c = True
    d = True
    try:
        result = system_state_checker(a, b, c, d)
        print(result)
    except ValueError as e:
        print(e)