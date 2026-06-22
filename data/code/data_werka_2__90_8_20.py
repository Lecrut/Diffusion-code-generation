def check_condition(*args):
    if not args:
        return False
    state_map = {
        'active': True,
        'inactive': False
    }
    current_state = state_map['inactive']
    for val in args:
        if val:
            current_state = state_map['active']
            break
    return current_state

if __name__ == '__main__':
    result = check_condition(False, False, True, False)
    print(result)