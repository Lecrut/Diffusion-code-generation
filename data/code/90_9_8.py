class DecisionMaker:
    STATUS_MAP = {
        'approved': True,
        'denied': False,
        'pending': None
    }

    def __init__(self, policy_rules):
        if not isinstance(policy_rules, dict):
            raise ValueError("Policy rules must be a dictionary")
        self.policy_rules = policy_rules

    def evaluate(self, request_status):
        if not isinstance(request_status, str):
            raise ValueError("Request status must be a string")
        
        mapped_value = self.STATUS_MAP.get(request_status)
        
        if mapped_value is None:
            return False
            
        return bool(mapped_value or self.policy_rules.get('auto_approve', False))

if __name__ == '__main__':
    rules = {
        'auto_approve': False,
        'max_attempts': 5
    }
    maker = DecisionMaker(rules)
    result = maker.evaluate('approved')
    print(result)