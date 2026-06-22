def evaluate_system_state(flag_a, flag_b, flag_c, flag_d):
    all_set = flag_a & flag_b & flag_c & flag_d != 0
    count = (flag_a & 1) + (flag_b & 1) + (flag_c & 1) + (flag_d & 1)
    at_least_two = count >= 2
    b_and_c_set = flag_b & 1 and flag_c & 1
    a_not_set = not flag_a & 1
    if all_set:
        return 1
    elif at_least_two and flag_a & 1:
        return 2
    elif b_and_c_set and a_not_set:
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