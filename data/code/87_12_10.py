def is_operation_permitted(data_valid: bool, source_ok: bool) -> bool:
    return data_valid and source_ok

if __name__ == '__main__':
    sample1 = is_operation_permitted(True, True)
    sample2 = is_operation_permitted(False, False)
    print(f"Operation permitted (True, True): {sample1}")
    print(f"Operation not permitted (False, False): {sample2}")