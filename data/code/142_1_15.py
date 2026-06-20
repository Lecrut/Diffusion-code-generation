def compare_boolean_results(a: bool, b: bool) -> str:
    assert isinstance(a, bool), "First input must be a boolean."
    assert isinstance(b, bool), "Second input must be a boolean."

    return "The boolean results are equal." if a == b else "The boolean results are different."

if __name__ == '__main__':
    result1 = compare_boolean_results(True, True)
    print(result1)
    result2 = compare_boolean_results(False, False)
    print(result2)
    result3 = compare_boolean_results(True, False)
    print(result3)
    result4 = compare_boolean_results(False, True)
    print(result4)