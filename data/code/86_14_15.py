BOOLEAN_EQUIVALENCE = 1

def bitwise_logical_comparison(a: bool, b: bool) -> int:
    return BOOLEAN_EQUIVALENCE if a == b else 0
if __name__ == '__main__':
    print(bitwise_logical_comparison(True, True))
    print(bitwise_logical_comparison(True, False))
    print(bitwise_logical_comparison(False, False))
    print(bitwise_logical_comparison(False, True))