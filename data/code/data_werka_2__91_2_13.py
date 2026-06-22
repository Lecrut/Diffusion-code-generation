def get_inverted_active_state(current_state):
    inverted = not current_state
    return inverted

if __name__ == '__main__':
    is_active = False
    final_output = get_inverted_active_state(is_active)
    print(final_output)