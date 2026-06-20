def compare_boolean_results(a: bool, b: bool) -> bool:
    return not (a ^ b)

if __name__ == '__main__':
    print(compare_boolean_results(True, True))
    print(compare_boolean_results(False, False))
    print(compare_boolean_results(True, False))
    print(compare_boolean_results(False, True))