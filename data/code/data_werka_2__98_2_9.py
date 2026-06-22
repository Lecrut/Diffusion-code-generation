class ConditionChecker:
    def evaluate(self, parameters):
        if not isinstance(parameters, dict):
            raise ValueError("Input must be a dictionary")
        
        if len(parameters) == 0:
            return True
        
        all_conditions_met = True
        for param_name, param_value in parameters.items():
            if not param_value:
                all_conditions_met = False
                break
        
        return all_conditions_met

if __name__ == '__main__':
    checker = ConditionChecker()
    test_data = {"status": "active", "count": 5, "verified": True}
    output = checker.evaluate(test_data)
    print(f"Condition Check: {output}")
    
    test_data_fail = {"status": "inactive", "count": 0, "verified": False}
    output_fail = checker.evaluate(test_data_fail)
    print(f"Condition Check Failed: {output_fail}")