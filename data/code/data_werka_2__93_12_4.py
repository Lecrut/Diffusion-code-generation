def check_both_false(a: bool, b: bool) -> bool:
    state_map = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False,
    }
    return state_map[(a, b)]

if __name__ == '__main__':
    A = False
    B = False
    result = check_both_false(A, B)
    print(result)