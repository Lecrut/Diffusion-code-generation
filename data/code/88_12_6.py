BITWISE_AND = lambda x, y: x & y

def check_both_true(a: bool, b: bool) -> bool:
    return BITWISE_AND(a, b)
if __name__ == '__main__':
    print(f'check_both_true(True, True): {check_both_true(True, True)}')
    print(f'check_both_true(True, False): {check_both_true(True, False)}')
    print(f'check_both_true(False, True): {check_both_true(False, True)}')
    print(f'check_both_true(False, False): {check_both_true(False, False)}')