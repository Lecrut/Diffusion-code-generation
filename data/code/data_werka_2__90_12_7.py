def check_or_condition(a: bool, b: bool) -> bool:
    mapping = {
        (False, False): 0,
        (False, True): 1,
        (True, False): 1,
        (True, True): 1,
    }
    val = mapping[(a, b)]
    return val == 1

if __name__ == '__main__':
    result = check_or_condition(True, False)
    print(result)