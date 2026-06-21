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
            elif isinstance(condition, tuple):
                if len(condition) != 2:
                    raise ValueError("Condition tuple must have exactly two elements")
                op, target = condition
                if op == '==':
                    if value != target:
                        return False
                elif op == '!=':
                    if value == target:
                        return False
                elif op == '>':
                    if not (value > target):
                        return False
                elif op == '<':
                    if not (value < target):
                        return False
                elif op == '>=':
                    if not (value >= target):
                        return False
                elif op == '<=':
                    if not (value <= target):
                        return False
                elif op == 'in':
                    if value not in target:
                        return False
                elif op == 'not in':
                    if value in target:
                        return False
                else:
                    raise ValueError(f"Unsupported operator: {op}")
            else:
                raise ValueError("Condition must be callable or tuple")
        
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    
    params1 = {
        'values': {'age': 25, 'score': 85},
        'conditions': {
            'age': ('>=', 18),
            'score': ('>', 80)
        }
    }
    result1 = checker.evaluate(params1)
    print(result1)
    
    params2 = {
        'values': {'age': 15, 'score': 90},
        'conditions': {
            'age': ('>=', 18),
            'score': ('>', 80)
        }
    }
    result2 = checker.evaluate(params2)
    print(result2)
    
    params3 = {
        'values': {'status': 'active'},
        'conditions': {
            'status': lambda x: x == 'active'
        }
    }
    result3 = checker.evaluate(params3)
    print(result3)