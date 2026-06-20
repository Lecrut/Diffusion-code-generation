class BooleanChecker:
    def __init__(self, values):
        self.values = values

    def check_at_least_one(self):
        return any(self.values)

if __name__ == '__main__':
    checker1 = BooleanChecker([False, False, False])
    print(f"list1: {checker1.check_at_least_one()}")

    checker2 = BooleanChecker([True, False, False])
    print(f"list2: {checker2.check_at_least_one()}")

    checker3 = BooleanChecker([])
    print(f"list3: {checker3.check_at_least_one()}")