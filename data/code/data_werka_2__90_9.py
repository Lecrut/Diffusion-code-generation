class DecisionMaker:
    def __init__(self, criteria):
        self.criteria = criteria

    def evaluate(self, action):
        if not isinstance(action, str):
            raise ValueError("Action must be a string")
        if not isinstance(self.criteria, dict):
            raise ValueError("Criteria must be a dictionary")
        
        for key, value in self.criteria.items():
            if value:
                return True
        return False

if __name__ == '__main__':
    decision_maker = DecisionMaker({'is_admin': False, 'has_permission': True, 'is_expired': False})
    result = decision_maker.evaluate('access_granted')
    print(result)