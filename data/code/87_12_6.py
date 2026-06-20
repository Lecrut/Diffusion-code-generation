def check_permissions(data_valid: bool, source_ok: bool) -> bool:
    return data_valid and source_ok

if __name__ == '__main__':
    sample1 = check_permissions(True, True)
    print(f"check_permissions(True, True): {sample1}")
    sample2 = check_permissions(False, False)
    print(f"check_permissions(False, False): {sample2}")