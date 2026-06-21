def negate_boolean(value: bool) -> bool:
    if not isinstance(value, bool):
        raise ValueError("Input must be a boolean")
    int_val = 1 if value else 0
    result_int = int_val ^ 1
    return bool(result_int)

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))