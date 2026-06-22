class DecisionMaker:
    def __init__(self, rules):
        if not isinstance(rules, dict):
            raise ValueError("Rules must be a dictionary mapping actions to criteria lists.")
        self.rules = rules

    def evaluate(self, action, context):
        if not isinstance(action, str):
            raise ValueError("Action must be a string.")
        if not isinstance(context, dict):
            raise ValueError("Context must be a dictionary.")
        
        if action not in self.rules:
            return False
        
        criteria_list = self.rules[action]
        
        for criteria in criteria_list:
            if not isinstance(criteria, dict):
                continue
            
            all_match = True
            for key, required_value in criteria.items():
                actual_value = context.get(key, None)
                if actual_value != required_value:
                    all_match = False
                    break
            
            if all_match:
                return True
        
        return False

if __name__ == '__main__':
    rules_config = {
        'deploy': [
            {'is_production': True, 'approved_by_lead': True},
            {'is_staging': True, 'approved_by_lead': False}
        ]
    }
    
    maker = DecisionMaker(rules_config)
    
    context_1 = {'is_production': True, 'approved_by_lead': True, 'is_staging': False}
    result_1 = maker.evaluate('deploy', context_1)
    print(result_1)
    
    context_2 = {'is_production': False, 'approved_by_lead': True, 'is_staging': True}
    result_2 = maker.evaluate('deploy', context_2)
    print(result_2)