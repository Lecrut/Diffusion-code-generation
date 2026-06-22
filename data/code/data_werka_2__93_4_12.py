def determine_both_false(val1, val2):
    def is_truthy(v):
        if v is None:
            return False
        if isinstance(v, bool):
            return v
        if isinstance(v, (int, float)):
            return v != 0
        if isinstance(v, str):
            return len(v) > 0
        if hasattr(v, '__len__'):
            return len(v) > 0
        return bool(v)

    truth1 = is_truthy(val1)
    truth2 = is_truthy(val2)
    return not truth1 and not truth2

if __name__ == '__main__':
    result = determine_both_false(0, 0)
    print(result)
    result2 = determine_both_false(1, 0)
    print(result2)
    result3 = determine_both_false(None, None)
    print(result3)
    result4 = determine_both_false([], {})
    print(result4)
    result5 = determine_both_false([1], {1: 1})
    print(result5)