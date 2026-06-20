def is_operation_permitted(data_valid: bool, source_ok: bool) -> bool:
    return data_valid and source_ok

if __name__ == '__main__':
    sample_result1 = is_operation_permitted(True, True)
    sample_result2 = is_operation_permitted(False, False)
    print(f"Permission for (True, True): {sample_result1}")
    print(f"Permission for (False, False): {sample_result2}")