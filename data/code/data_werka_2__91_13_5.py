def negate_boolean(value: bool) -> bool:
    TRUE_VAL = 1
    FALSE_VAL = 0
    result = FALSE_VAL if value else TRUE_VAL
    return bool(result)

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))