class DecisionMaker:

    def evaluate(self, condition1, condition2):
        if not isinstance(condition1, bool) or not isinstance(condition2, bool):
            raise ValueError('Both inputs must be boolean values.')
        return condition1 or condition2
if __name__ == '__main__':
    dm = DecisionMaker()
    print(dm.evaluate(True, False))
    print(dm.evaluate(False, False))
    print(dm.evaluate(True, True))