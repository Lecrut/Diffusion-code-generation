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
            
            val = values[key]
            
            if isinstance(condition, dict):
                op = condition.get('op')
                expected = condition.get('val')
                
                if op == 'eq':
                    if val != expected:
                        return False
                elif op == 'gt':
                    if not (val > expected):
                        return False
                elif op == 'lt':
                    if not (val < expected):
                        return False
                elif op == 'gte':
                    if not (val >= expected):
                        return False
                elif op == 'lte':
                    if not (val <= expected):
                        return False
                elif op == 'neq':
                    if val == expected:
                        return False
                else:
                    raise ValueError(f"Unsupported operator: {op}")
            elif callable(condition):
                if not condition(val):
                    return False
            else:
                if val != condition:
                    return False
        
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    
    params1 = {
        'conditions': {
            'age': {'op': 'gte', 'val': 18},
            'score': {'op': 'gt', 'val': 50}
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
            'age': {'op': 'gte', 'val': 18},
            'score': {'op': 'gt', 'val': 50}
        },
        'values': {
            'age': 15,
            'score': 75
        }
    }
    
    result2 = checker.evaluate(params2)
    print(result2)