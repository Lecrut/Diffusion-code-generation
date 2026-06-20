def check_equivalence(a: bool, b: bool) -> str:
    equivalence_map = {
        (True, True): 'Equal',
        (False, False): 'Equal',
        (True, False): 'One is True, the other is False',
        (False, True): 'One is True, the other is False'
    }
    return equivalence_map[(a, b)]

if __name__ == '__main__':
    print(check_equivalence(True, True))
    print(check_equivalence(True, False))
    print(check_equivalence(False, True))
    print(check_equivalence(False, False))