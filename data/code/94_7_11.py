class BooleanChecker:
    def __init__(self, boolean_list):
        self.boolean_list = boolean_list

    def check_any_true(self):
        return any(self.boolean_list)

if __name__ == '__main__':
    checker1 = BooleanChecker([False, False, False, True, False])
    print(f"List 1: {checker1.check_any_true()}")

    checker2 = BooleanChecker([False, False, False])
    print(f"List 2: {checker2.check_any_true()}")

    checker3 = BooleanChecker([True, True, True])
    print(f"List 3: {checker3.check_any_true()}")

    checker4 = BooleanChecker([])
    print(f"List 4: {checker4.check_any_true()}")

    checker5 = BooleanChecker([False])
    print(f"List 5: {checker5.check_any_true()}")