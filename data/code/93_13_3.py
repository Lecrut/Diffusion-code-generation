def check_both_false(a: bool, b: bool) -> bool:
    lookup = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False,
    }
    return lookup[(a, b)]

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)