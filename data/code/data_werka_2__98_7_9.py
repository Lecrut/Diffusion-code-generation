def evaluate_system_state(flag_a, flag_b, flag_c, flag_d):
    all_set = flag_a & flag_b & flag_c & flag_d
    count = (flag_a or 0) + (flag_b or 0) + (flag_c or 0) + (flag_d or 0)
    at_least_two = count >= 2
    condition_2 = at_least_two and flag_a
    condition_3 = flag_b and flag_c and (not flag_a)
    if all_set:
        return 1
    elif condition_2:
        return 2
    elif condition_3:
        return 3
    else:
        return 4
if __name__ == '__main__':
    result1 = evaluate_system_state(1, 1, 1, 1)
    print(result1)
    result2 = evaluate_system_state(1, 1, 0, 0)
    print(result2)
    result3 = evaluate_system_state(0, 1, 1, 0)
    print(result3)
    result4 = evaluate_system_state(0, 0, 0, 1)
    print(result4)