def get_negated_state(flag):
    if not isinstance(flag, bool):
        raise ValueError("Input must be a boolean")
    return not flag

if __name__ == '__main__':
    is_active = True
    print(get_negated_state(is_active))