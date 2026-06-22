def are_both_false(a: bool, b: bool) -> bool:
    truth_table = {
        (False, False): True,
        (False, True): False,
        (True, False): False,
        (True, True): False,
    }
    if a not in (True, False):
        raise ValueError("a must be a boolean")
    if b not in (True, False):
        raise ValueError("b must be a boolean")
    return truth_table[(a, b)]

if __name__ == '__main__':
    A = False
    B = False
    result = are_both_false(A, B)
    print(result)