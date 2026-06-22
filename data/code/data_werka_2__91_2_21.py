def invert_flag(current_state):
    inverted_state = not current_state
    return inverted_state

if __name__ == '__main__':
    is_active = False
    computed_result = invert_flag(is_active)
    print(computed_result)