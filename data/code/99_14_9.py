def validate_states(state1, state2, state3):
    return state1 and (not state2) or (not state1 and state3)
if __name__ == '__main__':
    print(validate_states(True, False, True))
    print(validate_states(False, True, False))