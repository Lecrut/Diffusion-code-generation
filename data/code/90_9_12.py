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
            elif hasattr(criterion, '__bool__'):
                result = result or bool(criterion)
            else:
                result = result or True
        
        return result

if __name__ == '__main__':
    dm = DecisionMaker()
    criteria1 = [False, False, True]
    criteria2 = [0, 0, 0]
    criteria3 = ["", "", "valid"]
    
    result1 = dm.evaluate(criteria1)
    result2 = dm.evaluate(criteria2)
    result3 = dm.evaluate(criteria3)
    
    print(result1)
    print(result2)
    print(result3)