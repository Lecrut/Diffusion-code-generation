def is_operation_permitted(data_valid: bool, source_ok: bool) -> bool:
    if not isinstance(data_valid, bool) or not isinstance(source_ok, bool):
        raise ValueError("Both data_valid and source_ok must be boolean values")
    
    return data_valid and source_ok

if __name__ == '__main__':
    print(is_operation_permitted(True, True))
    print(is_operation_permitted(False, False))
    print(is_operation_permitted(True, False))
    print(is_operation_permitted(False, True))