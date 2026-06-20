class TruthChecker:
    def __init__(self, iterable):
        self.iterable = iterable

    def check_any_true(self):
        return any(self.iterable)

if __name__ == '__main__':
    checker1 = TruthChecker([False, False, True, False])
    print(f"list1: {checker1.check_any_true()}")

    checker2 = TruthChecker([False, False, False])
    print(f"list2: {checker2.check_any_true()}")

    checker3 = TruthChecker([True])
    print(f"list3: {checker3.check_any_true()}")

    checker4 = TruthChecker([])
    print(f"list4: {checker4.check_any_true()}")