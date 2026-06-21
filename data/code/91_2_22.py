def get_negated_active_state(is_active):
    return not is_active

if __name__ == '__main__':
    is_active = True
    print(get_negated_active_state(is_active))