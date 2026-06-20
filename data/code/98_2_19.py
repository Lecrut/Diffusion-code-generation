class ConditionChecker:
    def evaluate(self, parameters):
        if not parameters:
            return True
        
        for key, condition in parameters.items():
            if callable(condition) and not condition():
                return False
            if not callable(condition) and not condition:
                return False
        
        return True

if __name__ == '__main__':
    checker = ConditionChecker()
    
    sample1 = {"a": lambda: True, "b": 10}
    result1 = checker.evaluate(sample1)
    print(f"Sample 1 Result: {result1}")
    
    sample2 = {"a": lambda: False, "b": 10}
    result2 = checker.evaluate(sample2)
    print(f"Sample 2 Result: {result2}")
    
    sample3 = {"a": True, "b": lambda: False}
    result3 = checker.evaluate(sample3)
    print(f"Sample 3 Result: {result3}")
    
    sample4 = {}
    result4 = checker.evaluate(sample4)
    print(f"Sample 4 Result: {result4}")