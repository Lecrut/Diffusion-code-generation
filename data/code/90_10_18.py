class DecisionMaker:

    def evaluate(self, criteria1, criteria2):
        return criteria1 or criteria2
if __name__ == '__main__':
    dm = DecisionMaker()
    print(dm.evaluate(True, False))
    print(dm.evaluate(False, True))
    print(dm.evaluate(False, False))