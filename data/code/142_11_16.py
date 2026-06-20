def check_equivalence(a: bool, b: bool) -> str:
    if a == b:
        return 'Equal'
    else:
        return 'One is True, the other is False'

if __name__ == '__main__':
    result = check_equivalence(True, False)
    print(result)