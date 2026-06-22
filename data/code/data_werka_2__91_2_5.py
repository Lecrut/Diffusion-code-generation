def toggle_active_state(current_state):
    inverted_state = not current_state
    return inverted_state

if __name__ == '__main__':
    is_active = False
    output_value = toggle_active_state(is_active)
    print(output_value)