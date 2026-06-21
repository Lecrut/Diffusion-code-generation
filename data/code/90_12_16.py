def check_or_condition(a: bool, b: bool) -> bool:
    lookup = {
        (False, False): False,
        (False, True): True,
        (True, False): True,
        (True, True): True,
    }
    return lookup[(a, b)]

if __name__ == '__main__':
    result = check_or_condition(True, False)
    print(result)