def get_negated_active_state(current_state):
    if not isinstance(current_state, bool):
        raise ValueError("Input must be a boolean")
    return not current_state

if __name__ == '__main__':
    is_active = True
    print(get_negated_active_state(is_active))