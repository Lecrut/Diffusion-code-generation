def is_operation_permitted(data_valid: bool, source_ok: bool) -> bool:
    if not isinstance(data_valid, bool):
        raise ValueError("data_valid must be a boolean")
    if not isinstance(source_ok, bool):
        raise ValueError("source_ok must be a boolean")
    
    return data_valid and source_ok

if __name__ == '__main__':
    print(is_operation_permitted(True, True))
    print(is_operation_permitted(False, False))