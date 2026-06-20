def compare_boolean_results(a: bool, b: bool) -> int:
    return 1 if a == b else 0
if __name__ == '__main__':
    print(compare_boolean_results(True, True))
    print(compare_boolean_results(False, False))
    print(compare_boolean_results(True, False))
    print(compare_boolean_results(False, True))