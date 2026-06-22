class DecisionMaker:
    MAX_RETRIES = 3
    DEFAULT_TIMEOUT = 30

    def __init__(self, criteria):
        if not isinstance(criteria, dict):
            raise ValueError("Criteria must be a dictionary")
        self.criteria = criteria

    def evaluate(self, action):
        if not isinstance(action, str):
            raise ValueError("Action must be a string")
        
        if not self.criteria:
            return False

        for value in self.criteria.values():
            if value:
                return True
        
        return False

if __name__ == '__main__':
    criteria = {
        'is_admin': False,
        'has_permission': True,
        'is_expired': False
    }
    
    decision_maker = DecisionMaker(criteria)
    result = decision_maker.evaluate('access_granted')
    print(result)