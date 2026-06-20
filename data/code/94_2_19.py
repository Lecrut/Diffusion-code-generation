class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        if not all(isinstance(item, bool) for item in boolean_list):
            raise ValueError("All elements in the list must be boolean values.")
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    print(f"List [False, False, True]: {checker.has_at_least_one_true([False, False, True])}")
    print(f"List [False, False, False]: {checker.has_at_least_one_true([False, False, False])}")
    print(f"List [True, True, True]: {checker.has_at_least_one_true([True, True, True])}")
    print(f"List [False, 'a', True]: {checker.has_at_least_one_true([False, 'a', True])}")