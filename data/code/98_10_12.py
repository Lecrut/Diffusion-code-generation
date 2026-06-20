class ConditionChecker:
    def check_all(self):
        conditions = [
            lambda: True,
            lambda: False,
            lambda: 1 == 1,
            lambda: "hello" == "hello",
            lambda: [1, 2, 3] == [1, 2, 3]
        ]
        return all(condition() for condition in conditions)

if __name__ == '__main__':
    checker = ConditionChecker()
    print(checker.check_all())