class ConditionChecker:
    def check_condition(self, a, b):
        return a == b

if __name__ == '__main__':
    sample_values = {
        'case1': (5, 5),
        'case2': (10, 20),
        'case3': (-1, -1),
        'case4': ('hello', 'hello'),
        'case5': ([], [])
    }
    
    checker = ConditionChecker()
    
    for key, (a, b) in sample_values.items():
        result = checker.check_condition(a, b)
        print(f"{key}: {result}")