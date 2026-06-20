class DecisionMaker:
    def evaluate(self, criteria):
        return any(criteria)

if __name__ == '__main__':
    decision_maker = DecisionMaker()
    sample_criteria1 = [False, False, True]
    print("Sample Criteria 1:", decision_maker.evaluate(sample_criteria1))
    
    sample_criteria2 = [True, False, False]
    print("Sample Criteria 2:", decision_maker.evaluate(sample_criteria2))
    
    sample_criteria3 = [False, False, False]
    print("Sample Criteria 3:", decision_maker.evaluate(sample_criteria3))