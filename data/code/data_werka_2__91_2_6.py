IS_ACTIVE_DEFAULT = True

def invert_state(flag):
    if flag is None:
        raise ValueError("Input must be a boolean")
    if flag:
        return False
    return True

if __name__ == '__main__':
    is_active = IS_ACTIVE_DEFAULT
    print(invert_state(is_active))