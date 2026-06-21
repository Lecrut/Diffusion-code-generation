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
            
            if callable(condition):
                if not condition(value):
                    return False
            elif isinstance(condition, dict):
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
                    if not (value in target):
                        return False
                elif op == 'not_in':
                    if value in target:
                        return False
                elif op == 'type':
                    if not isinstance(value, target):
                        return False
                elif op == 'regex':
                    import re
                    if not re.search(target, str(value)):
                        return False
                else:
                    raise ValueError(f"Unsupported operator: {op}")
            else:
                if value != condition:
                    return False
        
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    
    params1 = {
        'values': {
            'age': 25,
            'name': 'Alice',
            'score': 85
        },
        'conditions': {
            'age': {'op': 'gte', 'target': 18},
            'name': 'Alice',
            'score': lambda x: x > 80
        }
    }
    
    result1 = checker.evaluate(params1)
    print(result1)
    
    params2 = {
        'values': {
            'age': 15,
            'name': 'Bob'
        },
        'conditions': {
            'age': {'op': 'gte', 'target': 18},
            'name': 'Alice'
        }
    }
    
    result2 = checker.evaluate(params2)
    print(result2)
    
    params3 = {
        'values': {
            'status': 'active',
            'level': 3
        },
        'conditions': {
            'status': {'op': 'in', 'target': ['active', 'pending']},
            'level': {'op': 'type', 'target': int}
        }
    }
    
    result3 = checker.evaluate(params3)
    print(result3)