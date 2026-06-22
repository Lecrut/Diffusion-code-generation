class BooleanUniformityChecker:
    UNIFORM_TRUE = "all_true"
    UNIFORM_FALSE = "all_false"
    MIXED = "mixed"
    EMPTY = "empty"

    @staticmethod
    def _classify(values):
        if not values:
            return BooleanUniformityChecker.EMPTY
        first = values[0]
        if first:
            for val in values:
                if not val:
                    return BooleanUniformityChecker.MIXED
            return BooleanUniformityChecker.UNIFORM_TRUE
        else:
            for val in values:
                if val:
                    return BooleanUniformityChecker.MIXED
            return BooleanUniformityChecker.UNIFORM_FALSE

    def check_all_true(self, values):
        if not values:
            return False
        for val in values:
            if not val:
                return False
        return True

    def check_all_false(self, values):
        if not values:
            return False
        for val in values:
            if val:
                return False
        return True

    def check_uniformity(self, values):
        return self._classify(values)

if __name__ == '__main__':
    checker = BooleanUniformityChecker()
    true_list = [True, True, True]
    false_list = [False, False, False]
    mixed_list = [True, False, True]
    empty_list = []

    print(checker.check_all_true(true_list))
    print(checker.check_all_false(false_list))
    print(checker.check_uniformity(mixed_list))
    print(checker.check_uniformity(empty_list))