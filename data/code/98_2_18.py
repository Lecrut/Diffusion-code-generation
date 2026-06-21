class ConditionChecker:
    def evaluate(self, params):
        if not isinstance(params, dict):
            raise ValueError("Input must be a dictionary")
        
        conditions = params.get('conditions', {})
        values = params.get('values', {})
        
        if not conditions:
            return None
        
        for key, condition in conditions.items():
            if key not in values:
                return False
            
            value = values[key]
            
            if isinstance(condition, dict):
                op = condition.get('op')
                target = condition.get('target')
                
                if op == 'eq':
                    if value != target:
                        return False
                elif op == 'ne':
                    if value == target:
                        return False
                elif op == 'gt':
                    if not (value > target):
                        return False
                elif op == 'gte':
                    if not (value >= target):
                        return False
                elif op == 'lt':
                    if not (value < target):
                        return False
                elif op == 'lte':
                    if not (value <= target):
                        return False
                elif op == 'in':
                    if value not in target:
                        return False
                elif op == 'not_in':
                    if value in target:
                        return False
                else:
                    raise ValueError(f"Unsupported operator: {op}")
            else:
                if not value:
                    return False
        
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    
    sample_params = {
        'values': {
            'age': 25,
            'name': 'Alice',
            'score': 85
        },
        'conditions': {
            'age': {'op': 'gte', 'target': 18},
            'name': {'op': 'eq', 'target': 'Alice'},
            'score': {'op': 'gt', 'target': 80}
        }
    }
    
    result = checker.evaluate(sample_params)
    print(result)
    
    sample_params_fail = {
        'values': {
            'age': 15,
            'name': 'Bob',
            'score': 75
        },
        'conditions': {
            'age': {'op': 'gte', 'target': 18},
            'name': {'op': 'eq', 'target': 'Alice'},
            'score': {'op': 'gt', 'target': 80}
        }
    }
    
    result_fail = checker.evaluate(sample_params_fail)
    print(result_fail)