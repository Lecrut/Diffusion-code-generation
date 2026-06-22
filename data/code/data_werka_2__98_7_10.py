def evaluate_system_state(flag_a, flag_b, flag_c, flag_d):
    all_set = flag_a & flag_b & flag_c & flag_d
    count = flag_a + flag_b + flag_c + flag_d
    at_least_two = count >= 2
    flag_a_set = bool(flag_a)
    flag_b_set = bool(flag_b)
    flag_d_unset = not bool(flag_d)
    if all_set:
        return 1
    elif at_least_two and flag_a_set:
        return 2
    elif flag_b_set and flag_d_unset:
        return 3
    else:
        return 0
if __name__ == '__main__':
    result = evaluate_system_state(1, 1, 1, 1)
    print(result)
    result2 = evaluate_system_state(1, 1, 0, 0)
    print(result2)
    result3 = evaluate_system_state(0, 1, 0, 0)
    print(result3)
    result4 = evaluate_system_state(0, 0, 0, 0)
    print(result4)