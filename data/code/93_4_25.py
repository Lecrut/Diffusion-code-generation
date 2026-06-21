def determine_both_false(val1, val2):
    class BooleanWrapper:
        def __init__(self, value):
            self.value = value

        def is_truthy(self):
            try:
                return bool(self.value)
            except Exception:
                return False

    wrapper1 = BooleanWrapper(val1)
    wrapper2 = BooleanWrapper(val2)

    truth1 = wrapper1.is_truthy()
    truth2 = wrapper2.is_truthy()

    return not truth1 and not truth2

if __name__ == '__main__':
    result = determine_both_false(0, 0)
    print(result)
    result2 = determine_both_false(1, 1)
    print(result2)
    result3 = determine_both_false(None, [])
    print(result3)
    result4 = determine_both_false(True, False)
    print(result4)
    result5 = determine_both_false([], {})
    print(result5)