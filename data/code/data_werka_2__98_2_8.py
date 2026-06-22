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
                elif op == 'gt':
                    if not (value > target):
                        return False
                elif op == 'lt':
                    if not (value < target):
                        return False
                elif op == 'gte':
                    if not (value >= target):
                        return False
                elif op == 'lte':
                    if not (value <= target):
                        return False
                elif op == 'neq':
                    if value == target:
                        return False
                else:
                    raise ValueError(f"Unsupported operator: {op}")
            elif callable(condition):
                if not condition(value):
                    return False
            else:
                if value != condition:
                    return False
        
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    
    params1 = {
        'conditions': {
            'age': {'op': 'gte', 'target': 18},
            'score': {'op': 'gt', 'target': 50}
        },
        'values': {
            'age': 20,
            'score': 75
        }
    }
    
    result1 = checker.evaluate(params1)
    print(result1)
    
    params2 = {
        'conditions': {
            'age': {'op': 'gte', 'target': 18},
            'score': {'op': 'gt', 'target': 50}
        },
        'values': {
            'age': 15,
            'score': 75
        }
    }
    
    result2 = checker.evaluate(params2)
    print(result2)