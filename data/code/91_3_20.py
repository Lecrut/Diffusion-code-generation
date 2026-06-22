def negate_boolean(value: bool) -> bool:
    if value:
        return False
    return True

def bitwise_negate_boolean(value: bool) -> bool:
    return bool(~value)

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))
    print(bitwise_negate_boolean(True))
    print(bitwise_negate_boolean(False))