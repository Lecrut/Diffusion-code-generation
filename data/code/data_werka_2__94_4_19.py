class BooleanChecker:
    EMPTY_LIST_STATUS = False
    HAS_TRUE_STATUS = True

    @staticmethod
    def _verify_non_empty(data_list):
        if not data_list:
            return BooleanChecker.EMPTY_LIST_STATUS
        return True

    @staticmethod
    def _scan_for_true(data_list):
        iterator = iter(data_list)
        while True:
            try:
                item = next(iterator)
                if item:
                    return BooleanChecker.HAS_TRUE_STATUS
            except StopIteration:
                return BooleanChecker.EMPTY_LIST_STATUS

    @staticmethod
    def check_existence(data_list):
        if not BooleanChecker._verify_non_empty(data_list):
            return BooleanChecker.EMPTY_LIST_STATUS
        return BooleanChecker._scan_for_true(data_list)

if __name__ == '__main__':
    samples = [
        [False, False, False],
        [False, True, False],
        [],
        [True, True, True],
        [False],
        [False, False, True, False]
    ]
    for sample in samples:
        result = BooleanChecker.check_existence(sample)
        print(result)