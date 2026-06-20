class ConditionChecker:

    def check_all(self):
        conditions = [self.condition_1(), self.condition_2(), self.condition_3()]
        return all(conditions)

    def condition_1(self):
        return True

    def condition_2(self):
        return False

    def condition_3(self):
        return True
if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_all())