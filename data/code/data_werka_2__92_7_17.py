def invert_boolean(value: bool) -> bool:
    truthy = bool(value)
    inverted = not truthy
    return inverted

if __name__ == '__main__':
    original_flag = False
    flipped_flag = invert_boolean(original_flag)
    print(flipped_flag)