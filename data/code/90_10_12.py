class DecisionMaker:
    def evaluate(self, criteria):
        return any(criteria)

if __name__ == '__main__':
    decision_maker = DecisionMaker()
    
    sample_criteria1 = [True, False, True]
    print(f"Sample Criteria 1: {sample_criteria1}")
    print(f"Decision: {decision_maker.evaluate(sample_criteria1)}")
    
    sample_criteria2 = [False, False, False]
    print(f"\nSample Criteria 2: {sample_criteria2}")
    print(f"Decision: {decision_maker.evaluate(sample_criteria2)}")
    
    sample_criteria3 = [True, True, False]
    print(f"\nSample Criteria 3: {sample_criteria3}")
    print(f"Decision: {decision_maker.evaluate(sample_criteria3)}")