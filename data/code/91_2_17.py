def get_inverted_active_state(current_status: bool) -> bool:
    inverted_flag = not current_status
    return inverted_flag

if __name__ == '__main__':
    is_active = False
    computed_output = get_inverted_active_state(is_active)
    print(computed_output)