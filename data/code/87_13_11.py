def check_conditions(a: bool, b: bool) -> bool:
    conditions = {
        (True, False): True,
        (False, True): True,
        (True, True): False,
        (False, False): False
    }
    return conditions[(a, b)]

if __name__ == '__main__':
    print(check_conditions(True, False))
    print(check_conditions(False, True))
    print(check_conditions(True, True))
    print(check_conditions(False, False))