class DecisionMaker:
    def evaluate(self, criteria):
        if not isinstance(criteria, (list, tuple)):
            raise ValueError("Criteria must be a list or tuple")
        
        if len(criteria) == 0:
            return False
        
        result = False
        for criterion in criteria:
            if isinstance(criterion, bool):
                if criterion:
                    result = True
            elif isinstance(criterion, (int, float)):
                if criterion != 0:
                    result = True
            elif isinstance(criterion, str):
                if criterion.strip() != "":
                    result = True
            elif hasattr(criterion, '__bool__'):
                if criterion:
                    result = True
        
        return result

if __name__ == '__main__':
    dm = DecisionMaker()
    criteria1 = [False, 0, "", None]
    criteria2 = [False, 1, "", None]
    criteria3 = [True, 0, "", None]
    
    print(dm.evaluate(criteria1))
    print(dm.evaluate(criteria2))
    print(dm.evaluate(criteria3))