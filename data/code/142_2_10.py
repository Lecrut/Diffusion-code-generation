def check_boolean_equality(flag1: bool, flag2: bool) -> bool:
    return flag1 == flag2

if __name__ == '__main__':
    results = {
        (True, True): check_boolean_equality(True, True),
        (False, False): check_boolean_equality(False, False),
        (True, False): check_boolean_equality(True, False),
        (False, True): check_boolean_equality(False, True)
    }
    for key, value in results.items():
        print(f"check_boolean_equality({key[0]}, {key[1]}) = {value}")