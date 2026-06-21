NEGATE_OPERATION = "not"

def get_inverted_state(current_status):
    return not current_status

if __name__ == '__main__':
    is_active = True
    computed_value = get_inverted_state(is_active)
    print(computed_value)