class BooleanChecker:
    _RESULT_MAP = {
        True: "present",
        False: "absent"
    }

    def has_at_least_one_true(self, boolean_list):
        if not isinstance(boolean_list, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        for item in boolean_list:
            if item is True:
                return True
        return False

if __name__ == '__main__':
    checker = BooleanChecker()
    samples = [
        [False, False, False],
        [False, True, False],
        [True, True, False],
        [],
        [False]
    ]
    for idx, sample in enumerate(samples):
        result = checker.has_at_least_one_true(sample)
        status = BooleanChecker._RESULT_MAP[result]
        print(f"Sample {idx + 1}: {result} ({status})")