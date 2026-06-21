def invert_boolean(value: bool) -> bool:
    true_val = True
    false_val = False
    if value is true_val:
        return false_val
    return true_val

if __name__ == '__main__':
    flag = False
    inverted = invert_boolean(flag)
    print(inverted)
    flag = True
    inverted = invert_boolean(flag)
    print(inverted)