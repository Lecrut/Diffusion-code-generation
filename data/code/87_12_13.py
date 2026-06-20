PERMISSION_THRESHOLD = True

def is_operation_permitted(data_valid: bool, source_ok: bool) -> bool:
    return data_valid and source_ok >= PERMISSION_THRESHOLD

if __name__ == '__main__':
    print(is_operation_permitted(True, True))
    print(is_operation_permitted(False, True))
    print(is_operation_permitted(True, False))
    print(is_operation_permitted(False, False))