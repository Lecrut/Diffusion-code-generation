def get_negated_active_state(current_state):
    negated_state = not current_state
    return negated_state

if __name__ == '__main__':
    is_active = False
    computed_value = get_negated_active_state(is_active)
    print(computed_value)