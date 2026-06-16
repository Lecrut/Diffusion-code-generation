class DecisionEngine:
    def evaluate(self, data):
        rules = [
            {
                'condition': lambda x: x.get('age', 0) >= 18 and x.get('income', 0) > 50000,
                'action': 'approved'
            },
            {
                'condition': lambda x: x.get('status') == 'verified' and not x.get('flagged'),
                'action': 'active'
            },
            {
                'condition': lambda x: x.get('balance', 0) < -100,
                'action': 'alerted'
            }
        ]
        for rule in rules:
            if rule['condition'](data):
                return {'status': rule['action'], 'rule_id': list(rules).index(rule)}
        return {'status': 'default', 'rule_id': -1}
if __name__ == '__main__':
    test_cases = [
        {
            'age': 25,
            'income': 60000,
            'status': 'verified',
            'flagged': False,
            'balance': 5000
        },
        {
            'age': 17,
            'income': 80000,
            'status': 'pending'
        },
        {
            'balance': -200
        }
    ]
    engine = DecisionEngine()
    for i, case in enumerate(test_cases):
        result = engine.evaluate(case)
        print(f"Case {i + 1}: {result}")