class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    print(checker.has_at_least_one_true([False, False, True]))
    print(checker.has_at_least_one_true([False, False, False]))