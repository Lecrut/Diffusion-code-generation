class DecisionMaker:
    def __init__(self, rules):
        self.rules = rules

    def evaluate(self, context):
        if not isinstance(context, dict):
            raise ValueError("Context must be a dictionary")
        if not isinstance(self.rules, dict):
            raise ValueError("Rules must be a dictionary")
        
        results = []
        for rule_name, rule_value in self.rules.items():
            if rule_name in context:
                context_value = context[rule_name]
                if rule_value:
                    results.append(context_value)
        
        if not results:
            return False
        
        return any(results)

if __name__ == '__main__':
    rules_config = {
        'has_ticket': 'has_ticket',
        'is_member': 'is_member',
        'is_guest': 'is_guest'
    }
    dm = DecisionMaker(rules_config)
    sample_context = {
        'has_ticket': False,
        'is_member': False,
        'is_guest': True
    }
    outcome = dm.evaluate(sample_context)
    print(outcome)