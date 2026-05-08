def compare_boolean_results(a, b):
    if a == b:
        return "The boolean results are equal."
    else:
        return "The boolean results are different."
if __name__ == '__main__':
    result1 = compare_boolean_results(True, True)
    print(result1)
    result2 = compare_boolean_results(False, True)
    print(result2)
    result3 = compare_boolean_results(False, False)
    print(result3)