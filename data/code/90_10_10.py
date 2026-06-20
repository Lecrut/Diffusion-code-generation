class DecisionMaker:
    def evaluate(self, criteria):
        return any(criteria)

if __name__ == '__main__':
    decision_maker = DecisionMaker()
    sample_criteria = [False, False, True]
    print(decision_maker.evaluate(sample_criteria))