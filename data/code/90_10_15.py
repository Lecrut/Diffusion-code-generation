class DecisionMaker:

    def evaluate(self, condition1, condition2):
        return condition1 or condition2
if __name__ == '__main__':
    dm = DecisionMaker()
    print(dm.evaluate(True, False))
    print(dm.evaluate(False, True))
    print(dm.evaluate(False, False))