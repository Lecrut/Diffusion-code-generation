def check_permissions(data_valid: bool, source_ok: bool) -> bool:
    return data_valid and source_ok

if __name__ == '__main__':
    print(check_permissions(True, True))
    print(check_permissions(False, False))