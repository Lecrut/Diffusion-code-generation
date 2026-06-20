class BooleanChecker:
    def has_at_least_one_true(self, boolean_list):
        return any(boolean_list)

if __name__ == '__main__':
    checker = BooleanChecker()
    print(f"List 1: {checker.has_at_least_one_true([False, False, False])}")
    print(f"List 2: {checker.has_at_least_one_true([False, True, False])}")
    print(f"List 3: {checker.has_at_least_one_true([True, True, False])}")
    print(f"List 4: {checker.has_at_least_one_true([])}")
    print(f"List 5: {checker.has_at_least_one_true([False])}")