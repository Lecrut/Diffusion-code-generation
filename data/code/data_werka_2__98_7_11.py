def evaluate_system_state(flag_a: int, flag_b: int, flag_c: int, flag_d: int) -> int:
    if flag_a | flag_b | flag_c | flag_d == 0:
        return 0
    bit_a = flag_a & 1
    bit_b = flag_b & 2
    bit_c = flag_c & 4
    bit_d = flag_d & 8
    state = 0
    if bit_a:
        state += 1
    if bit_b:
        state += 2
    if bit_c:
        state += 4
    if bit_d:
        state += 8
    return state
if __name__ == '__main__':
    result = evaluate_system_state(1, 2, 0, 8)
    print(result)
    result2 = evaluate_system_state(0, 0, 4, 0)
    print(result2)
    result3 = evaluate_system_state(1, 1, 1, 1)
    print(result3)
    result4 = evaluate_system_state(0, 0, 0, 0)
    print(result4)