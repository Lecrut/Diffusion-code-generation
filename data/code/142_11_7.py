EQUIVALENT = True
NOT_EQUivalent = False

def check_equivalence(a: bool, b: bool) -> str:
    if a == b:
        return 'Equal'
    else:
        return 'One is True, the other is False'

if __name__ == '__main__':
    print(check_equivalence(True, True))
    print(check_equivalence(True, False))
    print(check_equivalence(False, True))
    print(check_equivalence(False, False))