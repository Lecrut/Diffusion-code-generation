class BooleanListChecker:
    def __init__(self, boolean_list):
        self.boolean_list = boolean_list

    def any_true(self):
        return any(self.boolean_list)

if __name__ == '__main__':
    checker1 = BooleanListChecker([False, False, False, True, False])
    print(f"List 1: {checker1.any_true()}")

    checker2 = BooleanListChecker([False, False, False])
    print(f"List 2: {checker2.any_true()}")

    checker3 = BooleanListChecker([True, True, True])
    print(f"List 3: {checker3.any_true()}")

    checker4 = BooleanListChecker([])
    print(f"List 4: {checker4.any_true()}")

    checker5 = BooleanListChecker([False])
    print(f"List 5: {checker5.any_true()}")