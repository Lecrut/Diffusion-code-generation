class DecisionMaker:
    def evaluate(self, criteria):
        return any(criteria)

if __name__ == '__main__':
    dm = DecisionMaker()
    sample_criteria = [False, False, True]
    print(dm.evaluate(sample_criteria))