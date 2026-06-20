class ExistenceChecker:
    def __init__(self, data_list):
        self.data_list = data_list

    def check(self):
        if not self.data_list:
            return False
        for item in self.data_list:
            if item:
                return True
        return False

if __name__ == '__main__':
    checker1 = ExistenceChecker([False, False, False])
    checker2 = ExistenceChecker([False, True, False])
    checker3 = ExistenceChecker([])
    checker4 = ExistenceChecker([True])

    print(f"list1: {checker1.check()}")
    print(f"list2: {checker2.check()}")
    print(f"list3: {checker3.check()}")
    print(f"list4: {checker4.check()}")