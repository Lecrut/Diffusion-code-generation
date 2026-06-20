def operation_permitted(data_valid: bool, source_ok: bool) -> bool:
    if data_valid and source_ok:
        return True
    else:
        return False

if __name__ == '__main__':
    result1 = operation_permitted(True, True)
    print(f"operation_permitted(True, True): {result1}")
    result2 = operation_permitted(False, True)
    print(f"operation_permitted(False, True): {result2}")
    result3 = operation_permitted(True, False)
    print(f"operation_permitted(True, False): {result3}")
    result4 = operation_permitted(False, False)
    print(f"operation_permitted(False, False): {result4}")