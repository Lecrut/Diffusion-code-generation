class DecisionMaker:
    def __init__(self, criteria):
        self.criteria = criteria

    def evaluate(self, action):
        if not isinstance(action, str):
            raise ValueError("Action must be a string")
        
        if action not in self.criteria:
            return False
        
        criteria_values = self.criteria[action]
        
        if not isinstance(criteria_values, (list, tuple)):
            raise ValueError("Criteria values must be a list or tuple")
        
        if len(criteria_values) == 0:
            return False
        
        result = False
        for value in criteria_values:
            if value:
                result = True
                break
        
        return result

if __name__ == '__main__':
    criteria = {
        'login': [False, True, False],
        'purchase': [False, False, False],
        'admin_access': [True, False, False]
    }
    
    maker = DecisionMaker(criteria)
    
    print(maker.evaluate('login'))
    print(maker.evaluate('purchase'))
    print(maker.evaluate('admin_access'))