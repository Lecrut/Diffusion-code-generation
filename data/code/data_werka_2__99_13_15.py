def validate_states(state_a: bool, state_b: bool, state_c: bool) -> bool:
    if not state_a:
        return False
    if state_b:
        return True
    return state_c
if __name__ == '__main__':
    result = validate_states(True, False, True)
    print(result)
    result2 = validate_states(False, True, True)
    print(result2)
    result3 = validate_states(True, True, False)
    print(result3)
    result4 = validate_states(True, False, False)
    print(result4)