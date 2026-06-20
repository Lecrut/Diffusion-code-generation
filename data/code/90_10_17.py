class DecisionMaker:
    def evaluate(self, criteria):
        return any(criteria)

if __name__ == '__main__':
    decision_maker = DecisionMaker()
    sample_criteria1 = [True, False, True]
    print(f"Sample Criteria 1: {sample_criteria1} -> {decision_maker.evaluate(sample_criteria1)}")
    sample_criteria2 = [False, False, False]
    print(f"Sample Criteria 2: {sample_criteria2} -> {decision_maker.evaluate(sample_criteria2)}")