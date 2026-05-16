def check_permission(data_valid: bool, source_ok: bool) -> bool:
    return data_valid and source_ok
if __name__ == '__main__':
    result1 = check_permission(True, True)
    print(f"Test 1 (True, True): {result1}")
    result2 = check_permission(True, False)
    print(f"Test 2 (True, False): {result2}")
    result3 = check_permission(False, True)
    print(f"Test 3 (False, True): {result3}")
    result4 = check_permission(False, False)
    print(f"Test 4 (False, False): {result4}")