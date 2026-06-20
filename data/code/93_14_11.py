BITWISE_AND = lambda x, y: x & y

def check_both_false(a: bool, b: bool) -> bool:
    return not BITWISE_AND(a, b)
if __name__ == '__main__':
    print(check_both_false(False, False))
    print(check_both_false(True, False))
    print(check_both_false(False, True))
    print(check_both_false(True, True))