equivalence_map = {
    (True, True): True,
    (False, False): True,
    (True, False): False,
    (False, True): False
}

def check_equivalence(a: bool, b: bool) -> bool:
    return equivalence_map[(a, b)]

if __name__ == '__main__':
    print(check_equivalence(True, True))
    print(check_equivalence(True, False))
    print(check_equivalence(False, True))
    print(check_equivalence(False, False))