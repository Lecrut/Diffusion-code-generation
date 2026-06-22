class DecisionMaker:
    def evaluate(self, criteria):
        if not isinstance(criteria, (list, tuple, set)):
            raise ValueError("Criteria must be an iterable of boolean values.")
        
        if not criteria:
            return False
        
        for criterion in criteria:
            if not isinstance(criterion, bool):
                raise ValueError("All criteria must be boolean values.")
        
        return any(criteria)

if __name__ == '__main__':
    dm = DecisionMaker()
    
    criteria1 = [False, False, True]
    result1 = dm.evaluate(criteria1)
    print(result1)
    
    criteria2 = [False, False, False]
    result2 = dm.evaluate(criteria2)
    print(result2)