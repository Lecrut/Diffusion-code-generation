def compare_boolean_results(a: bool, b: bool) -> str:
    if a == b:
        return "The boolean results are equal."
    else:
        return "The boolean results are different."
if __name__ == '__main__':
    print(compare_boolean_results(True, True))
    print(compare_boolean_results(False, False))
    print(compare_boolean_results(True, False))
    print(compare_boolean_results(False, True))