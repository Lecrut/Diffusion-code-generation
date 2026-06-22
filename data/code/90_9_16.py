class DecisionMaker:
    def evaluate(self, criteria):
        if not isinstance(criteria, (list, tuple)):
            raise ValueError("Criteria must be a list or tuple")
        
        if len(criteria) == 0:
            return False
        
        result = False
        for criterion in criteria:
            if not isinstance(criterion, bool):
                raise ValueError("All criteria must be boolean values")
            result = result or criterion
        
        return result

if __name__ == '__main__':
    decision_maker = DecisionMaker()
    criteria = [False, True, False]
    result = decision_maker.evaluate(criteria)
    print(result)