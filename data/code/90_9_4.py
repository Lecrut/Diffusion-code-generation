class DecisionMaker:
    def evaluate(self, criteria):
        if not isinstance(criteria, (list, tuple)):
            raise ValueError("Criteria must be a list or tuple")
        
        if len(criteria) == 0:
            return False
        
        result = False
        for criterion in criteria:
            if isinstance(criterion, bool):
                result = result or criterion
            elif isinstance(criterion, (int, float)):
                result = result or (criterion != 0)
            elif isinstance(criterion, str):
                result = result or (criterion.strip() != "")
            elif criterion is None:
                result = result or False
            else:
                result = result or bool(criterion)
        
        return result

if __name__ == '__main__':
    dm = DecisionMaker()
    criteria1 = [False, False, True]
    criteria2 = [0, 0, 0]
    criteria3 = [None, "", False]
    
    print(dm.evaluate(criteria1))
    print(dm.evaluate(criteria2))
    print(dm.evaluate(criteria3))