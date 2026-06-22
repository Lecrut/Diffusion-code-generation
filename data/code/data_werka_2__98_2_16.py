class ConditionChecker:
    def evaluate(self, params):
        conditions = params.get('conditions', {})
        values = params.get('values', {})
        
        if not conditions:
            return False
        
        for key, condition in conditions.items():
            if key not in values:
                return False
            
            value = values[key]
            
            if isinstance(condition, dict):
                op = condition.get('op')
                expected = condition.get('val')
                
                if op is None or expected is None:
                    raise ValueError("Condition must have 'op' and 'val' keys")
                
                if op == 'eq':
                    if value != expected:
                        return False
                elif op == 'ne':
                    if value == expected:
                        return False
                elif op == 'gt':
                    if value <= expected:
                        return False
                elif op == 'lt':
                    if value >= expected:
                        return False
                elif op == 'gte':
                    if value < expected:
                        return False
                elif op == 'lte':
                    if value > expected:
                        return False
                elif op == 'in':
                    if value not in expected:
                        return False
                elif op == 'not_in':
                    if value in expected:
                        return False
                elif op == 'type':
                    if type(value) != expected:
                        return False
                elif op == 'is_none':
                    if value is not None:
                        return False
                elif op == 'is_not_none':
                    if value is None:
                        return False
                else:
                    raise ValueError(f"Unsupported operator: {op}")
            else:
                raise ValueError("Condition must be a dictionary")
        
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    
    params = {
        'values': {
            'age': 25,
            'name': 'Alice',
            'score': 85
        },
        'conditions': {
            'age': {'op': 'gte', 'val': 18},
            'name': {'op': 'eq', 'val': 'Alice'},
            'score': {'op': 'gt', 'val': 80}
        }
    }
    
    result = checker.evaluate(params)
    print(result)