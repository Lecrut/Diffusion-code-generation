def is_operation_permitted(data_valid: bool, source_ok: bool) -> bool:
    if not data_valid:
        return False
    if not source_ok:
        return False
    return True

if __name__ == '__main__':
    print(is_operation_permitted(True, True))
    print(is_operation_permitted(False, True))
    print(is_operation_permitted(True, False))
    print(is_operation_permitted(False, False))